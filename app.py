from flask import Flask, render_template, request


app = Flask(__name__)

def get_weather_data(city):
    API_KEY = 'f06da9067dbd6169123990f46f302645'
    url= f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'  
    r= request.get(url).json()
    return r


@app.route("/")
def index():
    print(get_weather_data('Guayaquil'))
    return render_template('index.html')







if __name__ == '__main__':
    app.run(debug=True)

    