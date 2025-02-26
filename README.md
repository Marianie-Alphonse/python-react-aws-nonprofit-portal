# python-react-aws-nonprofit-portal

Demonstrates a full-stack application architecture using Python, React, and AWS services (including free PostgreSQL).  This project provides a foundation for building scalable web applications for chruch / nonprofit / community management deployed on AWS (Free Tier eligible).

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Running with Docker (Local Development)](#running-the-development-server)
    - [Running Tests](#running-tests)
- [Database Setup](#database-setup)
- [Liquibase Migrations](#liquibase-migrations)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [Author](#author)

## Introduction

This project aims to provide a free and open-source platform for churches and non-profit organizations to manage their communities effectively. It simplifies tasks such as collecting donations, managing user accounts, and posting announcements, all within a user-friendly interface. The project is designed to be easily deployable on AWS using the Free Tier, making it accessible to organizations with limited budgets.

## Features

*   **Donation Management:** Securely process and track donations.
*   **User Management:** Manage user accounts, roles, and permissions. (
*   **Announcements:**  Post and manage announcements to keep the community informed. 
*   **Responsive Design:** Accessible on various devices (desktops, tablets, and phones).
*   **Tab-Based Navigation:** Easy navigation between different sections of the application.

## Tech Stack

*   **Frontend:** React, JavaScript, HTML, CSS,
*   **Backend:** Python, Flask
*   **Database:** PostgreSQL, AWS RDS
*   **Cloud Platform:** AWS (S3, Lambda, API Gateway, Cognito)
*   **Version Control:** Git
*   **Database Migrations:** Liquibase

## Getting Started

### Prerequisites

*   Node.js and npm (or yarn) for the frontend
*   Python 3.13 for the backend
*   AWS CLI configured with your credentials
*   PIP (Python package installer)
*   Docker Desktop
*   Git

### Installation

1.  Clone the repository: `git clone https://github.com/Marianie-Alphonse/python-react-aws-nonprofit-portal.git`
2.  Navigate to the frontend directory: `cd frontend`
3.  Install frontend dependencies: `npm install` or `yarn install`
4.  Navigate to the backend directory: `cd backend`
5.  Install backend dependencies: `pip install -r requirements.txt`

## Deployment

1.  Build the React app: `npm run build` or `yarn build` (in the frontend directory)
2.  Upload the contents of the `build` directory to your S3 bucket.
3.  Configure API Gateway to route requests to your Lambda functions.

### Running the Development Server

```bash
docker-compose up -d # Start all containers
```
This command starts all containers defined in docker-compose.yml in detached mode. This includes the PostgreSQL database, Liquibase migrations, your Flask backend, and the React frontend development server. This method is recommended for running the application locally on your computer.

1. Start Containers: Run the above command in your terminal from the project's root directory.

2. Access Frontend: Open your web browser and navigate to http://localhost:3000.

3. Access Backend: The Flask backend will be available at http://localhost:8000.

4. Database Connection: You can connect to the PostgreSQL database using localhost:5432 with the credentials specified in your docker-compose.yml file.

### Running Tests

```bash
cd frontend
npm test
```
This command will run the test suite for your React application. Make sure you have set up your tests appropriately.

## Database Setup

The database is set up using Docker Compose and PostgreSQL. The `docker-compose.yml` file defines the database service.

## Liquibase Migrations

Database schema changes are managed using Liquibase. The `liquibase` service in `docker-compose.yml` runs Liquibase migrations on container startup.

## Deployment

1.  Build the React app: `npm run build` or `yarn build` (in the frontend directory)
2.  Upload the contents of the `build` directory to your S3 bucket.
3.  Configure API Gateway to route requests to your Lambda functions.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Author

Marianie Alphonse

