

This is a Django-based API for managing real estate listings and reviews agents properties and their prices. It includes CRUD (Create, Read, Update, Delete) functionality for both listings and reviews, and provides a backend admin interface for managing the data.

## Table of Contents
- [Project Setup](#project-setup)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Testing](#testing)
- [API Endpoints](#api-endpoints)
- [Admin Interface](#admin-interface)

## Project Setup

**Clone the Repository:**

Create a Virtual Environment:
python -m venv venv

Activate the Virtual Environment:

On Windows:

venv\Scripts\activate

Install Dependencies:

pip install -r requirements.txt

pip install django djangorestframework

Create and Apply Migrations:

python manage.py makemigrations

python manage.py migrate

**Create a Superuser:**

python manage.py createsuperuser

**Running the Project**

python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser to access the application. For the admin interface, navigate to http://127.0.0.1:8000/admin/.

**Testing**

You can test CRUD functionality through the Django admin interface.

**API Endpoints**

The following endpoints are available:

##Listings:
GET /api/listings/ - List all listings
POST /api/listings/ - Create a new listing
GET /api/listings/<int:pk>/ - Retrieve a specific listing
PUT /api/listings/<int:pk>/ - Update a specific listing
DELETE /api/listings/<int:pk>/ - Delete a specific listing

Reviews:
GET /api/reviews/ - List all reviews
POST /api/reviews/ - Create a new review
GET /api/reviews/<int:pk>/ - Retrieve a specific review
PUT /api/reviews/<int:pk>/ - Update a specific review
DELETE /api/reviews/<int:pk>/ - Delete a specific review

**Admin Interface**
Log in to the admin interface at http://127.0.0.1:8000/admin/ using the superuser credentials created earlier. You can manage listings and reviews through this interface.
