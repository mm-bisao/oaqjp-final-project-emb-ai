import requests
import json

# Function to perform emotion detection
def emotion_detector(text_to_analyze):
    # Define the URL for the Watson Emotion Predict API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Define the headers required by the API
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Define the input data for the POST request
    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send the POST request to the Watson NLP API
    try:
        response = requests.post(url, headers=headers, json=data)
        
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Convert the response text into a dictionary (JSON)
            response_json = response.json()
            
            # Extract the emotion scores from the response
            emotions = response_json.get('emotion', {})

            # Extract the scores for each emotion
            anger_score = emotions.get('anger', 0)
            disgust_score = emotions.get('disgust', 0)
            fear_score = emotions.get('fear', 0)
            joy_score = emotions.get('joy', 0)
            sadness_score = emotions.get('sadness', 0)

            # Create a dictionary to store emotions and their scores
            emotion_scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }

            # Find the dominant emotion by finding the emotion with the highest score
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)

            # Add the dominant emotion to the dictionary
            emotion_scores['dominant_emotion'] = dominant_emotion

            # Return the emotion scores along with the dominant emotion
            return emotion_scores
        
        else:
            # Return error message if the response status code is not 200
            return f"Error: {response.status_code}, {response.text}"

    except Exception as e:
        # Handle exceptions, e.g., network issues or API problems
        return f"An error occurred: {str(e)}"


# Main function for testing or running the emotion detector
if __name__ == "__main__":
    # Sample text to be analyzed
    text_to_analyze = "I am feeling so happy and excited today!"

    # Call the emotion detector function
    result = emotion_detector(text_to_analyze)
    
    # Print the result (the emotions detected along with dominant emotion)
    print(json.dumps(result, indent=4))
