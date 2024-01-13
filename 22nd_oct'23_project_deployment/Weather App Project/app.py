from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/weatherapp', methods = ["POST","GET"])
def get_weatherdata():
    url = "https://api.openweathermap.org/data/2.5/weather"
    para = {'q':request.form.get("city"),
        'appid':request.form.get('appid'),
        'units':request.form.get('units')
        }
    response = requests.get(url ,params=para)
    data = response.json()
    return render_template('weather_result.html', weather_data=data)
    # else:
    #     return render_template('weather_search.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)