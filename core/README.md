# Internship Management System

A Django REST Framework API for managing Internship Applications

## Setup Instructions:

### 1. Create and activate a Virtual environment
python -m venv venv
venv\Scripts\activate
### 2. Run Migrations
python manage.py makemigration
python manage.py Migrate 

## Run the Project
Python manage.py runserver

The Api is available at http://127.0.0.1:8000/api/

## Running Tests
python manage.py tests

## Endpoints

POST  | /api/candidates/
GET   | /api/candidates/
POST  | /api/applications/
POST  | /api/applications/
GET   | /api/applications/
GET   | /api/applications/?staus=interview
POST  | /api/applications/<id>/notes
GET  | /api/applications/<id>/notes
GET  | /api/Summary

### Valid application statuses
applied, screening, interview, rejected, accepted

## Completion Status

all but one requirement are complete:
- All 3 models with correct fields and constraints
- All endpoints are implemented

## Not Implemented

- Unique email validation.
