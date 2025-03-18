from flask import Flask, render_template, request
from EmotionDetection import emotion_detector  # Import the emotion_detector function from the package

# Create a Flask application instance
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def emotionDetector():
    # Initialize result variables
    result = None
    emotion_data = None

    # If the request method is POST, process the form data
    if request.method == 'POST':
        text_to_analyze = request.form['statement']  # Get the input text from the form

        # Call the emotion_detector function from the EmotionDetection package
        result = emotion_detector(text_to_analyze)

        # If the dominant emotion is None, return an error message
        if result['dominant_emotion'] is None:
            return render_template('index.html', response="Invalid text! Please try again.")

        # Format the result as required in the task
        emotion_data = {
            'anger': result['anger'],
            'disgust': result['disgust'],
            'fear': result['fear'],
            'joy': result['joy'],
            'sadness': result['sadness'],
            'dominant_emotion': result['dominant_emotion']
        }

        response = f"For the given statement, the system response is 'anger': {emotion_data['anger']}, " \
                   f"'disgust': {emotion_data['disgust']}, 'fear': {emotion_data['fear']}, " \
                   f"'joy': {emotion_data['joy']} and 'sadness': {emotion_data['sadness']}. " \
                   f"The dominant emotion is {emotion_data['dominant_emotion']}."

        return render_template('index.html', response=response)

    return render_template('index.html', response=None)

# Run the Flask app on localhost:5000
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
