from flask import render_template
from application import app
import requests

@app.route('/')
@app.route('/home')
def home():
 return render_template('home.html', title='Button')

@app.route('/generate', methods=['GET','POST'])
def generateAnimal():
    response = requests.get('http://app2:5001/animal/name')
    noise = requests.post('http://app2:5001/animal/sound',data=response.text)
    return render_template('generate.html', animal_name=response.text, animal_noise=noise.text)
