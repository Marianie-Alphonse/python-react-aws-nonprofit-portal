FROM liquibase/liquibase:latest

COPY changelog/1.0.0.yaml /liquibase/changelog/1.0.0.yaml

RUN wget https://jdbc.postgresql.org/download/postgresql-42.7.1.jar -P /liquibase/lib

# Run Liquibase update on container startup
CMD ["update"]