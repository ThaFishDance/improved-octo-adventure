from flask import Flask, render_template, request, flash
import requests
app = Flask(__name__)
app.secret_key = b''

@app.route('/', methods = ['POST', 'GET'])
def hello_world():
    mainData = {}
    city = ''
    error = None
    if request.method == 'POST': 
        city = request.form['city'] 
        api_key = ""
        base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(base_url)
        if response.status_code == 400:
            flash('Please enter a city')
        elif response.status_code == 404:
            flash(f'{city} was not found. Please try again.')
        elif response.status_code == 200:
            responseData = response.json()
            mainData = responseData['main']
        else:
            pass
            
    return render_template('index.html', mainData=mainData, city=city)
