from flask import Flask, jsonify, request
from flask_cors import CORS
import numpy as np
import os
import librosa
from keras.models import load_model
app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
class_labels = ['Dove', 'Duck', 'Parrot', 'Eagle', 'Peacock']

bird_info = {
    'Dove': {
        'origin': 'Doves are found all over the world, except in the coldest regions.',
        'description': 'Doves are small to medium-sized birds that are typically around 12 inches (30 cm) long. They have a plump body, small head, and a short beak. Doves come in a range of colors, including gray, brown, and white. They are known for their soft cooing calls and are often kept as pets or used as symbols of peace and love.',
        'Scientific Name': 'Columdidae Colombiformes'
    },
    'Duck': {
        'origin': 'Ducks can be found all over the world, except in Antarctica.',
        'description': 'Ducks are medium-sized water birds that have a broad, flat bill, a rounded body, and webbed feet. They come in a variety of colors, including green, blue, brown, and white. Ducks are well adapted to swimming and diving, and are commonly hunted for their meat, eggs, and feathers.',
        'Scientific Name': 'Anatidae Anseriformes'
    },
    'Parrot': {
        'origin': 'Parrots are found in tropical and subtropical regions all over the world, including Central and South America, Africa, and Australia.',
        'description': 'Parrots are colorful birds with a curved beak, zygodactyl feet (two toes pointing forward and two backward), and a strong, hooked bill. They come in a range of colors, including green, blue, red, and yellow. Parrots are highly intelligent and are known for their ability to mimic human speech and sounds. They are often kept as pets and can live for several decades.',
        'Scientific Name': 'Phaethomtidae Psittaciformes'
    },
    'Eagle': {
        'origin': 'Eagles are found all over the world, except in Antarctica.',
        'description': 'Eagles are large birds of prey that have a powerful beak and talons, and broad, strong wings. They come in a range of colors, including brown, black, and white. Eagles are known for their keen eyesight and are often used as symbols of strength and freedom. They are also highly skilled hunters and feed on a variety of prey, including fish, mammals, and reptiles.',
        'Scientific Name': 'Aquila Accipitridae'
    },
    'Peacock': {
        'origin': 'Peacocks are native to South Asia, but are now found in many parts of the world, including North America, Europe, and Africa.',
        'description': 'Peacocks are medium-sized birds that are about 35-50 inches (90-125 cm) in length. They have a long, colorful tail with iridescent feathers that can be blue, green, or gold. The body is dark blue or green, and the head is adorned with a distinctive crest of feathers. Peacocks are known for their beautiful plumage, which is used to attract mates during mating season.',
        'Scientific Name': 'Pava Cristatus'
    }
}


@app.route("/getSong", methods=["POST"])
def hello_world():
    if request.method == "POST":
        file = request.files["file"]
        file.save("/tmp/song.mp3")
        audio, sr = librosa.load("/tmp/song.mp3", sr=None)
        mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
        if mfcc.shape[1] == 0:
            feature_vector = np.zeros((40,))
        else:
            mfcc_mean = np.mean(mfcc, axis=1)
            feature_vector = np.concatenate((mfcc_mean,))
        model = load_model(os.getcwd()+"/audio_classification.hdf5")
        x = np.reshape(feature_vector, (1, -1))
        predicted_class_index = model.predict(x)
        pred = np.argmax(predicted_class_index)
        predicted_class_label = class_labels[pred]
        bird_information = bird_info[predicted_class_label]
        return jsonify({"species": predicted_class_label, "origin": bird_information['origin'], "description": bird_information['description'], "scientific_name": bird_information['Scientific Name']})
