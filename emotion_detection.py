import requests
import json

def emotion_detector(text_to_analyze):
    # Check if the text is blank
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # The Watson NLP Emotion Predict API endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Headers for the API request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Prepare the input data
    input_data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Make a POST request to the Watson NLP API
    response = requests.post(url, headers=headers, json=input_data)

    # If the status code is 400 (Bad Request), return None values
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Otherwise, process the response and return the emotion scores
    try:
        result = response.json()

        anger_score = result.get('anger', 0)
        disgust_score = result.get('disgust', 0)
        fear_score = result.get('fear', 0)
        joy_score = result.get('joy', 0)
        sadness_score = result.get('sadness', 0)

        # Determine the dominant emotion
        emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }

        dominant_emotion = max(emotions, key=emotions.get)

        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    except Exception as e:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
