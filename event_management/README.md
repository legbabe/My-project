# Event Management API

## Overview
The **Event Management API** is a Django-based application that allows users to create, manage, and register for events, as well as receive notifications related to event activities.

## Features
- **User Authentication**: Register, login, and manage profiles.
- **Event Management**: Create, update, delete, and view events.
- **Event Registration**: Users can register for events with capacity limits.
- **Notifications**: Get notifications about event registrations and updates.

## Prerequisites
- **Python**: 3.12+
- **Django**: 4.x
- **PostgreSQL** or **SQLite**

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/event-management-api.git
   cd event-management-api
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

## Endpoints

### User Authentication

- **Register**: `POST /api/users/register/`
  ```json
  {
    "email": "user@example.com",
    "username": "username",
    "password": "password123"
  }
  ```

- **Login**: `POST /api/users/login/`
  ```json
  {
    "email": "user@example.com",
    "password": "password123"
  }
  ```


### Event Management

- **List Events**: `GET /api/events/`
- **Create Event**: `POST /api/events/`  
  _(Authenticated users only)_
  ```json
  {
    "name": "Event Name",
    "description": "Event Description",
    "start_time": "2024-10-01T10:00:00Z",
    "end_time": "2024-10-01T12:00:00Z",
    "location": "Event Location",
    "capacity": 50,
    "category": "Conference"
  }
  ```

- **Register for Event**: `POST /api/events/{event_id}/register/`  
  _(Authenticated users only)_

### Notifications

- **List Notifications**: `GET /api/notifications/`  
  _(Authenticated users only)_

## Authentication

This API uses **JWT (JSON Web Tokens)** for authentication. To access protected endpoints, follow these steps:

1. **Login** to get the access token using `/api/users/login/`:
   ```json
   {
     "email": "user@example.com",
     "password": "password123"
   }
   ```

2. Include the token in the `Authorization` header of requests to protected endpoints:
   ```
   Authorization: Bearer <your_access_token>
   ```
   curl -H "Authorization: Bearer your-access-token" \
     -X GET http://127.0.0.1:8000/api/events/


---
### API Documentation