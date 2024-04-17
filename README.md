# IAP-Group-project

# Group 22 - Contributors

- 1.Richard Karanu Mbuti - SCT212-0062/2019


# Job Application Tracker

## Overview

The Job Application Tracker is a Django-based web application designed to help users manage their job applications effectively. It allows users to track the status of their applications and provides companies with a platform to post job openings and review applications.

## Features

- **User Authentication**: Supports user registration, login, and logout functionalities.
- **Job Management**: Employers can post job vacancies, edit them, and delete them as needed.
- **Application Submission**: Job seekers can apply for jobs, upload resumes, and write cover letters.
- **Application Tracking**: Users can view the jobs they've applied for and track the status of each application.
- **Admin Dashboard**: Administrators can view all job listings and applications, and update the status of applications.

## Technologies

- **Django**: As the web framework.
- **SQLite**: Default database, easy to set up.
- **Bootstrap**: For responsive front-end design.

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- pip and virtualenv

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/veenjenga/IAP-Group-project
   cd job-application-tracker
   ```
2. **Create and activate a virtual environment:**
   ```bash
   virtualenv venv
   # On Windows use: .\venv\Scripts\activate
   # On Unix or MacOS use: source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
7. **Visit http://localhost:8000 to access the application.**

## Usage

- **Register:** First, create an account using the "Sign Up" link.
- **Log In:** Log in using your credentials.
- **Dashboard:** Access your dashboard to view or post jobs.
- **Apply for Jobs:** Click on any job listing to view details and apply.
- **Check Application Status:** Track the status updates of your applications from your dashboard.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests with your proposed changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
