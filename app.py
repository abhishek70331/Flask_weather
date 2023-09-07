from flask import Flask, request,render_template,url_for,redirect
import requests
app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])

def index():
    if request.method == "POST":
        city = request.form["city"]
        print(city)
        url= requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=f41d70e7042843693a778ff7d76768e9')
        response = url.json()

        description = response['weather'][0]['description']
        temp = response['main']['temp']
        humidity = response['main']['humidity']
        print(response)
        return render_template("index.html",city=city, description=description,temp=temp,humidity=humidity)
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run()