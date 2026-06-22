"""
Server module for the Emotion Detection application.
Executes Flask routes to interface with the Watson NLP client package.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emot_detector():
    """
    Retrieves query parameters, calls the backend analysis service,
    and returns a formatted string containing emotion scores or error feedback.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
        
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is **{response['dominant_emotion']}**."
    )

@app.route("/")
def render_index_page():
    """
    Renders the default web homepage layout template.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
