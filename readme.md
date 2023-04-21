Address Book API
This is an Address Book API that allows users to create, update, delete, and retrieve addresses. The API saves addresses to an SQLite database and validates them before saving. Users can also retrieve addresses within a given distance and location coordinates.

Getting Started
Prerequisites
Before running the application, make sure you have the following software installed:

Python 3.7 or higher
pip (Python package manager)
Installation
Clone this repository to your local machine.
Navigate to the project directory in your terminal.
Run pip install -r requirements.txt to install the required Python packages.
Running the Application
Navigate to the project directory in your terminal.
Run uvicorn app.main:app --reload to start the application.
Open your web browser and go to http://localhost:8000/docs to access the API documentation.
API Endpoints
The following endpoints are available in the Address Book API:

Create Address
Endpoint: /address

HTTP Method: POST

Request Body:

{
    "name": "John Doe",
    "address": "123 Main St, Anytown USA",
    "latitude": 40.7128,
    "longitude": -74.0060
}
Response Body:

{
    "id": 1,
    "name": "John Doe",
    "address": "123 Main St, Anytown USA",
    "latitude": 40.7128,
    "longitude": -74.0060
}
Update Address
Endpoint: /address/{address_id}

HTTP Method: PUT

Request Body:

{
    "name": "Jane Doe",
    "address": "456 Elm St, Othertown USA",
    "latitude": 37.7749,
    "longitude": -122.4194
}
Response Body:

{
    "id": 1,
    "name": "Jane Doe",
    "address": "456 Elm St, Othertown USA",
    "latitude": 37.7749,
    "longitude": -122.4194
}
Delete Address
Endpoint: /address/{address_id}

HTTP Method: DELETE

Response Body:

{
    "message": "Address with ID 1 deleted"
}
Retrieve Address
Endpoint: /address/{address_id}

HTTP Method: GET

Response Body:

{
    "id": 1,
    "name": "John Doe",
    "address": "123 Main St, Anytown USA",
    "latitude": 40.7128,
    "longitude": -74.0060
}
Retrieve Addresses within a Distance
Endpoint: /address/within/{distance}/of

HTTP Method: GET

Query Parameters:

latitude (required): the latitude of the center point
longitude (required): the longitude of the center point
Response Body:

[    {        "id": 1,        "name": "John Doe",        "address": "123 Main St, Anytown USA",        "latitude": 40.7128,        "longitude": -74.0060    },    {        "id": 2,        "name": "Jane Doe",        "address": "456 Elm St, Othertown USA",        "latitude": 37.7749,        "longitude": -122.4194    }]

Built With

Python 3.7
FastAPI
SQLite
GeoPy

To create a sample address_book.db database for the above code, you can use SQLite command-line shell. Follow these steps:

Open a terminal and navigate to the project directory.
Start the SQLite command-line shell by typing sqlite3 address_book.db.
Create the addresses table by typing the following command:

CREATE TABLE addresses (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL
);

Insert some sample data into the addresses table by typing the following command:

INSERT INTO addresses (name, address, latitude, longitude) VALUES
('John Doe', '123 Main St, Anytown USA', 40.7128, -74.0060),
('Jane Doe', '456 Elm St, Othertown USA', 37.7749, -122.4194),
('Bob Smith', '789 Oak St, Another Town USA', 34.0522, -118.2437);

This will insert 3 sample addresses with their names, addresses, and coordinates.
Exit the SQLite command-line shell by typing .exit.
Your address_book.db database is now ready. You can use it to test the API by connecting to it in code.


Here's how to execute the app:

Create a new directory for the project and navigate into it.
Create a virtual environment by running python -m venv env.
Activate the virtual environment by running source env/bin/activate on Unix/Linux or .\env\Scripts\activate on Windows.
Install the required libraries by running pip install fastapi fastapi_sqlalchemy[postgresql] pydantic geopy.
Create a file named main.py and copy the code for main.py, models/address.py, utils/distance.py, and routes/address.py into it.
Run the app by running uvicorn main:app --reload in the terminal.
Open your browser and navigate to http://localhost:8000/docs to view the Swagger documentation and test the API.