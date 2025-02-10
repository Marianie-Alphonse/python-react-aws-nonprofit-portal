# python-react-aws-nonprofit-portal

Demonstrates a full-stack application architecture using Python, React, and AWS services (including free PostgreSQL).  This project provides a foundation for building scalable web applications for chruch / nonprofit / community management deployed on AWS (Free Tier eligible).

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Deployment](#deployment)
- [Contributing](#contributing)

## Introduction

This project aims to provide a free and open-source platform for churches and non-profit organizations to manage their communities effectively. It simplifies tasks such as collecting donations, managing user accounts, and posting announcements, all within a user-friendly interface. The project is designed to be easily deployable on AWS using the Free Tier, making it accessible to organizations with limited budgets.

## Features

*   **Donation Management:** Securely process and track donations.
*   **User Management:** Manage user accounts, roles, and permissions. (
*   **Announcements:**  Post and manage announcements to keep the community informed. 

## Tech Stack

*   **Frontend:** React, JavaScript, HTML, CSS,
*   **Backend:** Python, Flask
*   **Database:** PostgreSQL, AWS RDS
*   **Cloud Platform:** AWS (S3, Lambda, API Gateway, Cognito)
*   **Version Control:** Git

## Getting Started

### Prerequisites

*   Node.js and npm (or yarn) for the frontend
*   Python 3.13 for the backend
*   AWS CLI configured with your credentials
*   Git

### Installation

1.  Clone the repository: `git clone https://github.com/your-username/your-repo-name.git`
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
cd frontend  # Navigate to the frontend directory
npm start    # Start the development server
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
