from flask import Flask, render_template, request
import requests
app = Flask(__name__)
import json

@app.route('/home')
def index():
    return render_template('home.html')


@app.route('/home', methods=['POST', 'GET'])
def data():
    if request.method=='POST':
        city = request.form['city']
        add_location=city
        apikey="7a25b655898f8bddca5b58c4ab4a4f51"
        url_get="http://api.openweathermap.org/data/2.5/weather?q="+add_location+"&appid="+apikey+"&units=metric"
        res=requests.get(url_get).status_code
        response=requests.get(url_get).text
        response=json.loads(response)
        print(response)
        if res==200:
            return render_template('home.html', weather = response["weather"][0]["main"], city = response["name"], country = response["sys"]["country"], temprature = response["main"]["temp"], min_temp = response["main"]["temp_min"], max_temp = response["main"]["temp_max"], humidity = response["main"]["humidity"], wind = response["wind"]["speed"])
        return render_template('home.html', result = "enter Correct city name")


if __name__ == '__main__':
    app.run(debug=True)
