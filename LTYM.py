from flask import Flask, jsonify
from flask_cors import CORS

from sentiment import get_emotions
from music import get_tracks


app = Flask(__name__)
CORS(app)


@app.route('/emotion/<sentence>', methods=['GET'])
def analyze_emotion(sentence):
    emotions = get_emotions(sentence)
    return jsonify(emotions)


@app.route('/music/<emotion>', methods=['GET'])
def get_music_recommendations(emotion):
    tracks = get_tracks(emotion)
    return jsonify(tracks)


if __name__ == '__main__':
    app.run(debug=False)
