# DorsaPrj

# Django REST Service

This is a Django REST service with three APIs: sum, all, and total.

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

    The history API returns all a and b that have been requested so far.
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

    Returns a JSON object containing the total of all a and b that have been requested so far.
    {
      "total": 10.0
    }

**Installation:**

    git clone https://github.com/BahramRousta/DorsaProject.git

    cd DorsaProject

    Install dependencies:
        pip install -r requirements.txt
    Run the server:
        python manage.py runserver

The server will start running at http://localhost:8000/.
