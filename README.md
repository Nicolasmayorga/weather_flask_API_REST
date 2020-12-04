## Rest API of Weather

This API REST is costructing in flask framewrok of django and is a simple example of a CRUD of the waether in the 3 procipal cities in Colombia.: Bogotá, Medellín and Cali. 

This content the data from https://api.openweathermap.org/ of December 3th of 2020 but give the illution of update data of the wather.

This API is content 3 files: 
    1. app.py that controling all the CRUD and the interaction with the API
    2. weather.py that contetn all the data for the API REST for the 3 cities and a forecast for the city of Medellín for the next 5 day
    3. dates.py that allow give the illution for update dates

## Requiments

1. Python 3.5 or upload
2. env
2. flask
3. pylint (optional)
4. insomnia or postman for the interaction with the CRUD with the API

## instruction

1. Download all the repository

2. Activate the env

3. Activate in your console the file app.py. This gonna run all the app and ON the localhots of Flask. This localhost is activate in the port 4000 and have the debug activate if you want use it.

4. For the interaction with the API you can go to http://127.0.0.1:4000/. If you want interac with the API you can go to http://127.0.0.1:4000/weather or http://127.0.0.1:4000/forecast for the forecast of Medellin.

If you want make interaction with one city specifically you can write the city after the endpoint weather. example  http://127.0.0.1:4000/weather/bogota 

5. For make inraction with the CRUD and create new cities you need the program postman or insomnia and have basic knowledge about them. 

Enjoy it !!

