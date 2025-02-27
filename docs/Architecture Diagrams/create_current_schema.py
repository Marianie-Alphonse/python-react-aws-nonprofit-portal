import re
from graphviz import Digraph

def extract_schema(yaml_content):
    schema = {}
    primary_keys = {}
    foreign_keys = {}

    create_table_pattern = re.compile(r'createTable:\s+tableName:\s+(\w+)')
    column_pattern = re.compile(r'name:\s+(\w+)')
    constraint_pattern = re.compile(r'constraints:\s+\{([^}]+)\}')
    references_pattern = re.compile(r'references:\s+(\w+\(\w+\))')

    create_table_matches = create_table_pattern.findall(yaml_content)

    for table_name in create_table_matches:
        schema[table_name] = []
        table_start = yaml_content.find(f'tableName: {table_name}')
        table_block = yaml_content[table_start : yaml_content.find('- changeSet', table_start+ 1)]

        columns = column_pattern.findall(table_block)

        for column in columns:
            schema[table_name].append(column)
            column_start = table_block.find(f'name: {column}')
            column_end = table_block.find('column:', column_start + 1) if table_block.find('column:', column_start + 1) != -1 else len(table_block)
            column_text = table_block[column_start:column_end]

            constraint_start = column_text.find('constraints:')
            constraint_end = column_text.find('column:', constraint_start + 1) if table_block.find('column:', constraint_start + 1) != -1 else table_block.find('- changeSet', constraint_start + 1)
            constraint = table_block[constraint_start:constraint_end]
            if constraint:
                if 'primaryKey: true' in constraint:
                    primary_keys[table_name] = column
                if 'foreignKey: true' in constraint:
                    references_match = references_pattern.search(constraint)
                    if references_match:
                        foreign_keys[table_name] = {
                            'column': column,
                            'references': references_match.group(1)
                        }

    return schema, primary_keys, foreign_keys

def generate_erd_image(schema, primary_keys, foreign_keys, output_filename):
    dot = Digraph(comment='Entity Relationship Diagram')

    # Add tables as nodes (rectangles)
    for table_name, columns in schema.items():
        table_label = f"<<TABLE BORDER=\"0\" CELLBORDER=\"1\" CELLSPACING=\"0\">"
        table_label += f"<TR><TD COLSPAN=\"2\" BGCOLOR=\"lightblue\">{table_name}</TD></TR>"
        for column in columns:
            if table_name in primary_keys and column == primary_keys[table_name]:
                table_label += f"<TR><TD ALIGN=\"LEFT\"><b>{column}</b></TD><TD ALIGN=\"LEFT\">PK</TD></TR>"
            elif table_name in foreign_keys and column == foreign_keys[table_name]['column']:
                table_label += f"<TR><TD ALIGN=\"LEFT\"><b>{column}</b></TD><TD ALIGN=\"LEFT\">FK</TD></TR>"
            else:
                table_label += f"<TR><TD ALIGN=\"LEFT\">{column}</TD><TD ALIGN=\"LEFT\"></TD></TR>"
        table_label += "</TABLE>>"
        dot.node(table_name, label=table_label, shape='rectangle')  # Added shape='rectangle'

    # Add relationships as edges
    print(foreign_keys)
    for table_name, fk_data in foreign_keys.items():
        if 'references' in fk_data:
            ref_table, ref_column = fk_data['references'].split('(')[0], fk_data['references'].split('(')[1][:-1]
            dot.edge(table_name, ref_table)

    dot.render(output_filename, format='png', cleanup=True)

def main():
    yaml_file_path = "../liquibase/changelog/1.0.0.yaml"  # Replace with your YAML file path

    try:
        with open(yaml_file_path, "r") as file:
            yaml_content = file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {yaml_file_path}")
        return

    schema, primary_keys, foreign_keys = extract_schema(yaml_content)
    generate_erd_image(schema, primary_keys, foreign_keys, "current_schema")

if __name__ == "__main__":
    main()