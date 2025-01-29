# Introduction
This a backend project that demonstrates how the REST framework can be implemented in Python using a micro framework Flask with its rest framework extension Flask-Restful.

## How to run the project 
Install the applications dependencies from requirements.txt

`pip install -r requirements.txt` 

Then in the project main directory run

`python server.py`

This will start the server listening at 'http://localhost:5000'. To access the resource required for this assignment make a GET request to the endpoint 'http://localhost:5000/me'.

## Documentation 

`GET /me`

An endpoint for accessing the 'me' resource object. Make a GET request to the  `/me` URL to get a JSON response containing email, current_datetime, and github url linking to this repository.


## Example usage 

1. Clone the project from 'https://github.com/ubterko/stage-zero'. And proceed to open a terminal at the directory of the app in your machine. 

2. Install the projects dependencies by entering the following in the apps main directory where you have requirements.txt.

   ```pip install -r requirements.txt```

3. Wait for the installations to complete then still in the project main directory run the following commands

     `python server.py`

    This will start the server listening at 'http://localhost:5000'. 

4. To access the resource required for this assignment make a GET request to the endpoint 'http://localhost:5000/me'. 

    This will return a json format data containing 'email', 'current_datetime' and the github url link to this project.

```
{ 
    "email": "ebonko2017ip@gmail.com",
    "current_datetime": 
    "github_url": "<https://github.com/ubterkostage-zero>"
}
```

## Looking to hire developers? 
Pick from our list of competent backend developers. Click one of the following links to find developers that match the desired skills for your projects. 

https://hng.tech/hire/python-developers
https://hng.tech/hire/csharp-developers
https://hng.tech/hire/golang-developers
https://hng.tech/hire/php-developers
https://hng.tech/hire/java-developers
https://hng.tech/hire/nodejs-developers