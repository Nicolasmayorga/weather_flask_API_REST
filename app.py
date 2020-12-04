from flask import Flask, jsonify, request

app = Flask(__name__)

from weather import weather, forecast

@app.route('/weather')
def getWeather():
    return jsonify({"Weather": weather, "message": "This is the weather for today"})

@app.route('/weather/<string:location_name>')
def getWeatherCity(location_name):
    cityFound = [city for city in weather if city['a_location_name'] == location_name]
    if (len(cityFound)> 0):
        return jsonify({'city': cityFound[0]})
    return jsonify({"message": "Product not found"})
    

@app.route('/weather', methods=['POST'])
def addWeather():
    new_city = {
        "a_location_name": request.json['a_location_name'],
        "a_country": request.json['a_country'],
        "date": request.json['date'],
        "temperature": request.json['temperature'],
        "wind": request.json['wind'],
        "pressure": request.json['pressure'],
        "humidity": request.json['humidity'],
        "sunrise": request.json['sunrise'],
        "sunset": request.json['sunset'],
        "geo_coordinates": request.json['geo_coordinates'],
        
    }
    weather.append(weather)
    return jsonify({"message": "Product add succesfull", "city": weather})

@app.route('/weather/<string:location_name>', methods=['PUT'])
def editProducts(location_name):
    cityFound = [city for city in weather if city['a_location_name'] == location_name]
    if (len(cityFound)> 0):
        cityFound[0]['a_location_name'] = request.json['a_location_name']
        cityFound[0]['a_country'] = request.json['a_country']
        cityFound[0]['date'] = request.json['date']
        cityFound[0]['temperature'] = request.json['temperature']
        cityFound[0]['wind'] = request.json['wind']
        cityFound[0]['pressure'] = request.json['pressure']
        cityFound[0]['humidity'] = request.json['humidity']
        cityFound[0]['sunrise'] = request.json['sunrise']
        cityFound[0]['geo_coordinates'] = request.json['geo_coordinates']
        
        return jsonify({
            "message": "City weather Updated",
            "City": cityFound
        })
        
    return jsonify({"message": "City not found"})


@app.route('/weather/<string:location_name>', methods=['DELETE'])
def deleteWeather(location_name):
    cityFound = [city for city in weather if city['a_location_name'] == location_name]
    if (len(cityFound)> 0):
        location_name.remove(cityFound[0])
        return jsonify({
            "Message": "City Deleted",
            "City": cityFound
        })
    return jsonify({"mesasge": "City not found"})


@app.route('/forecast')
def getForecast():
    return jsonify({"Forecast": forecast, "message": "This is the weather for the city of Medellin for the next 5 days at 3:00 p.m"})

if __name__ == "__main__":
    app.run(debug=True, port=4000)
    
