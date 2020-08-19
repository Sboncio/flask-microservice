from flask import Flask, Response, request, jsonify
from random import randint
app = Flask(__name__)

animals = ['lion','dog','elephant','cow','pig','fox']
animal_sounds = {'lion':'roar','dog':'bark','elephant':'Trumpet','cow':'moo','pig':'oink','fox':'ringdingdingdingding'}

@app.route('/text', methods=['GET'])
def get_text():
    return Response("This is my first API", mimetype='text/plain')

@app.route('/animal/name', methods=['GET'])
def post_animal():
    animal = str(animals[randint(0,5)])
    return Response(animal, mimetype='text/plain')

@app.route('/animal/sound', methods=['GET','POST'])
def animal_noise():
    data_sent = request.data.decode('utf-8')
    noise = animal_sounds[data_sent]
    return Response(noise, mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')
