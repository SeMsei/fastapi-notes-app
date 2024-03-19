# FastSpi Notes Api
This is a simaple API providing main functionality for Notes Application with user authentication and registration features.
## Features
* User registration and login functionality
* Personalized notes for each user
* Add, edit, and delete notes
## Technologies
* FastApi
* SQLite (for database)
* Bcrypt (for password encryption)
* Swagger (for api documentation)
## Getting Started
### Clone the repository:
* git clone https://github.com/SeMsei/flas-notes-app.git
### Navigate to the project directory:
* cd flask-notes-app
### Create and activate a virtual environment:
* python -m venv venv
* venv/bin/activate (On Windows, use - venv\Scripts\activate)
### Install dependencies:
* pip install -r requirements.txt
### Run the application:
* cd src/back
* uvicorn main:app
##
The app will be accessible at http://127.0.0.1:8000/ in your browser.
To check API documentation navigate to http://127.0.0.1:8000/docs

### Usage 
You use this API directly using PostMan, or swagger, or curl. Or you use it in ur application.
