from Flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(_name_)

@app.route("/emotionDetector")
def emot_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    # Handle the error scenario where dominant_emotion is None
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
        
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is *{response['dominant_emotion']}*."
    )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
