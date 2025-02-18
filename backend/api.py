rom flask import Flask, jsonify, request
import psycopg2  # For PostgreSQL database connection
import uuid  # For generating UUIDs

app = Flask(__name__)

# Helper function to connect to the database
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except psycopg2.Error as e:
        print(f"Database connection error: {e}")
        return None

# API Endpoints

@app.route('/api/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        cur = conn.cursor()
        cur.execute("SELECT user_id, first_name, last_name, email FROM users")
        users = cur.fetchall()
        user_list = []
        for user in users:
            user_list.append({
                "user_id": str(user[0]),  # Convert UUID to string
                "first_name": user[1],
                "last_name": user[2],
                "email": user[3]
            })
        cur.close()
        conn.close()
        return jsonify(user_list)
    except psycopg2.Error as e:
        print(f"Error fetching users: {e}")
        conn.close()
        return jsonify({"error": "Error fetching users"}), 500

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')

    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        cur = conn.cursor()
        user_id = uuid.uuid4() # Generate UUID
        cur.execute("INSERT INTO users (user_id, first_name, last_name, email) VALUES (%s, %s, %s, %s)",
                    (user_id, first_name, last_name, email))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"message": "User created", "user_id": str(user_id)}), 201  # Return the new user ID
    except psycopg2.Error as e:
        conn.rollback() # Important: Rollback on error
        print(f"Error creating user: {e}")
        conn.close()
        return jsonify({"error": "Error creating user"}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)