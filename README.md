# Django REST API for User CRUD Operations

This Django project provides a RESTful API for performing CRUD (Create, Read, Update, Delete) operations on User resources in a database. The API endpoints allow you to manage user information, including id, name, email, and password.

## Requirements

- Python 3.x
- Django 3.x
- Django REST framework
- MySQL database server
-  Virtual environment (recommended for isolation)

## Getting Started Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/pranita28Dane/RepairsDuniya-Assignment-Task
   ``` 
2. Navigate to the project directory:

   ```bash
   cd RepairsDuniya-Assignment-Task
   ```
3. Create and activate a virtual environment (optional but recommended):

  ```bash
  python -m venv venv
  source venv/bin/activate  
  On Windows, use `venv\Scripts\activate`
  ```

4. Install project dependencies:

  ```bash
  pip install -r requirements.txt
  ```

5. Perform database migrations:

  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

6. Configure the Database:

  - Open the settings.py file in the user_api directory.

  - Update the database settings to use your MySQL database server:
 
      ```bash
      DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'djangodb',  
        'USER': 'root',  
        'PASSWORD': '',  
        'HOST': 'localhost',  
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'STRICT_TRANS_TABLES',
        },
      }
    }

    ```
    
  - Replace the placeholders ('NAME', 'USER', 'PASSWORD', 'HOST', and 'PORT') with your actual MySQL database configuration.

 7.  Create a superuser (admin) to access the Django admin panel:

  ```bash
    python manage.py createsuperuser

    username: admin
    password: admin
  ```

8. Start the development server:

  ```bash
    python manage.py runserver
  ```
   
# API Endpoints
## Get a list of all users:
  - Endpoint: http://127.0.0.1:8000/users/
  - Method: GET
    
## Get a user by ID:
  - Endpoint: http://127.0.0.1:8000/users/5/
  - Method: GET
    
## Create a new user:
  - Endpoint: http://127.0.0.1:8000/users/create/
  - Method: POST
  - Request Body: JSON data with user information (name, email, password)
  - ```bash
    {
    "name": "John Doe",
    "email": "john@example.com",
    "password": "securepassword"
    }

    ```
    
## Delete a user by ID:
  - Endpoint: http://127.0.0.1:8000/users/delete/8/
  - Method: DELETE
    
# Testing with Postman
  1. Open Postman and create a new request for each of the API endpoints mentioned above.

  2. Set the appropriate HTTP method and URL for each request.

  3. For POST requests, provide JSON data in the request body to create a new user.

  4. Send the requests to test the CRUD operations on the User resource

# API Documentation
For API documentation and usage examples, please refer to the API Documentation file.     
