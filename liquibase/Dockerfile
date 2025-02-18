FROM liquibase/liquibase:latest

COPY liquibase/changelog /liquibase/changelog

# Set the database connection details as environment variables
ENV LIQUIBASE_URL jdbc:postgresql://db:5432/community_hub
ENV LIQUIBASE_USERNAME community_hub_user
ENV LIQUIBASE_PASSWORD community_hub_password

# Run Liquibase update on container startup
CMD ["update"]