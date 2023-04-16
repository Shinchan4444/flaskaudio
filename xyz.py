import os
import random
import string
import pyttsx3
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speak', methods=['POST'])
def speak():
    # Get the text to speak from the form data
    text = request.form['text']

    # Set up the text-to-speech engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 150) # Set speech rate (words per minute)
    
    # Generate a random filename for the audio file
    filename = ''.join(random.choices(string.ascii_lowercase, k=8)) + '.mp3'
    
    # Convert the text to speech and save to file
    engine.save_to_file(text, os.path.join('static', filename))
    engine.runAndWait()

    # Return the name of the saved file
    return filename

@app.route('/static/<path:path>')
def send_audio(path):
    return send_from_directory('static', path,mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(debug=True)
