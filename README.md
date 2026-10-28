# Healthcare Backend API

A healthcare management backend built with Django, Django REST Framework, PostgreSQL, and JWT authentication.

## Features

- User registration and login
- JWT access and refresh tokens
- Protected API endpoints
- Patient management
- Doctor management
- Patient–doctor assignment management
- Patient data ownership restrictions
- Django Admin dashboard
- Input validation and error handling

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- SimpleJWT
- python-dotenv

## Prerequisites

Install the following before running the project:

- Python
- PostgreSQL
- Git (optional)
- Postman for API testing

## Setup Instructions

### 1. Clone or download the project

Open a terminal in the project directory.

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

On Windows Git Bash:

```bash
source venv/Scripts/activate
```

### 3. Install dependencies

```bash
pip install django djangorestframework djangorestframework-simplejwt "psycopg[binary]" python-dotenv
```

### 4. Configure environment variables

Create a `.env` file in the same directory as `manage.py`.

```env
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=healthcare_db
DB_USER=healthcare_user
DB_PASSWORD=your-database-password
DB_HOST=127.0.0.1
DB_PORT=5432
```

Replace the example secret and database password with your own values.

### 5. Create the PostgreSQL database

Create a PostgreSQL database named `healthcare_db` and configure the database user and password to match your `.env` file.

### 6. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create an administrator account

```bash
python manage.py createsuperuser
```

Follow the prompts to configure your administrator account.

### 8. Start the development server

```bash
python manage.py runserver
```

The API will be available at:

`http://127.0.0.1:8000/`

The Django Admin dashboard is available at:

`http://127.0.0.1:8000/admin/`

## API Endpoints

All endpoints below use the `/api/` prefix.

| Method    | Endpoint                             | Description                  |
| --------- | ------------------------------------ | ---------------------------- |
| POST      | `/api/register/`                     | Register a user              |
| POST      | `/api/login/`                        | Obtain JWT tokens            |
| POST      | `/api/token/refresh/`                | Refresh an access token      |
| GET       | `/api/test-auth/`                    | Test JWT authentication      |
| GET       | `/api/patients/`                     | List accessible patients     |
| POST      | `/api/patients/`                     | Create a patient             |
| GET       | `/api/patients/{id}/`                | Retrieve a patient           |
| PUT/PATCH | `/api/patients/{id}/`                | Update a patient             |
| DELETE    | `/api/patients/{id}/`                | Delete a patient             |
| GET       | `/api/doctors/`                      | List doctors                 |
| POST      | `/api/doctors/`                      | Create a doctor              |
| GET       | `/api/doctors/{id}/`                 | Retrieve a doctor            |
| PUT/PATCH | `/api/doctors/{id}/`                 | Update a doctor              |
| DELETE    | `/api/doctors/{id}/`                 | Delete a doctor              |
| GET       | `/api/patient-doctor-mappings/`      | List accessible assignments  |
| POST      | `/api/patient-doctor-mappings/`      | Assign a doctor to a patient |
| GET       | `/api/patient-doctor-mappings/{id}/` | Retrieve an assignment       |
| PUT/PATCH | `/api/patient-doctor-mappings/{id}/` | Update an assignment         |
| DELETE    | `/api/patient-doctor-mappings/{id}/` | Remove an assignment         |

## Authentication

Use the login endpoint to obtain JWT tokens.

Example request:

```json
{
  "email": "your-email@example.com",
  "password": "your-password"
}
```

For protected endpoints, include the access token in the request header:

```text
Authorization: Bearer YOUR_ACCESS_TOKEN
```

Use the access token, not the refresh token, for API authentication.

## Example Requests

### Register a user

`POST /api/register/`

```json
{
  "email": "user@example.com",
  "first_name": "Rahul",
  "last_name": "Sharma",
  "password": "StrongPassword123"
}
```

### Create a patient

`POST /api/patients/`

```json
{
  "name": "Rahul Sharma",
  "age": 30,
  "gender": "Male",
  "address": "Delhi, India"
}
```

The authenticated user is assigned as the patient owner by the API.

### Create a doctor

`POST /api/doctors/`

```json
{
  "name": "Dr. Amit Sharma",
  "specialization": "Cardiology",
  "email": "amit.sharma@example.com",
  "phone": "9876543210",
  "address": "Delhi, India"
}
```

### Assign a doctor to a patient

`POST /api/patient-doctor-mappings/`

```json
{
  "patient": 1,
  "doctor": 1
}
```

Use existing patient and doctor IDs from your database.

## Validation and Security

- Passwords are stored using Django's password hashing.
- JWT authentication protects configured API endpoints.
- Patient records are restricted to their owners.
- Patient–doctor assignments are restricted to assignments associated with the logged-in user's patients.
- Patient age must be 120 or below.
- Duplicate patient–doctor assignments are prevented.
- Database credentials and the Django secret key are configured through environment variables.

## Testing

Use Postman to test the endpoints.

1. Register a user.
2. Log in and obtain an access token.
3. Create a patient using the access token.
4. Create a doctor using the access token.
5. Assign the doctor to the patient.
6. Verify that listing, updating, and deleting records work as expected.
7. Verify that invalid data and unauthenticated requests are rejected.

Run Django's system check with:

```bash
python manage.py check
```

## Project Status

The core API endpoints, JWT authentication, PostgreSQL integration, patient–doctor assignments, and Django Admin have been implemented and tested during development.

