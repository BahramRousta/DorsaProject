# DorsaPrj

# Django REST Service

This is a Django REST service with four APIs: sum, all, total and login.

**SUM API**:

    The sum API accepts two float parameters a and b and returns their sum. 

**Endpoint:**

    GET /sum

**Parameters:** 

| Parameter | Type | Description       |
|-----------|---------|-------------------|
| a  | float  | The first number  |
| b  | float  | The second number |



**Response:** 

    Returns a JSON object containing the sum of a and b:
    {
      "result": 3.14
    }

**HISTORY API:**

    The history API returns all a and b that have been requested so far. For reach to this api user must first login.
    
**Endpoint:**

    GET /history
    
**Response:** 

    Returns a JSON array containing all a and b that have been requested so far:
    [
      {"a": 1.0, "b": 2.0},
      {"a": 3.0, "b": 4.0}
    ]

**TOTAL API:** 

    The total API returns the total of all a and b that have been requested so far.
**Endpoint:**

    GET /total
**Response:** 

    Returns a JSON object containing the total of all a and b that have been requested so far. For reach to this api user must first login.
    {
      "total": 10.0
    }
    
**LOGIN API:** 

    The login API returns the access and refresh token and authenticated user.
    
**Endpoint:**

    POST /login
    
**Parameters:**    
    
| Parameter | Type | Description       |
|-----------|---------|-------------------|
| username  | string  | username  |
| password  | string  | password |
    
**Response:** 

    Returns a JSON object containing the access and rerfresh TOKEN.
    {
    "access_token": "access_token",
    "refresh_token": "refresh_token",
    }

**Installation:**

    git clone https://github.com/BahramRousta/DorsaProject.git

    cd DorsaProject
    
    create ENV and active it:
        python -m venv env
    install dependencies:
        pip install -r requirements.txt
    create db
        python manage.py makemigrations
        python manage.py migrate
    create superuser:
        python manage.py createsuperuser
    run the server:
        python manage.py runserver
    run test:
        pytest
        
The server will start running at http://localhost:8000/.
