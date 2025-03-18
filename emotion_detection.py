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
            # Get the JSON response and extract the emotion-related data
            response_json = response.json()
            return response_json  # You can return the whole response or any specific part of it
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
    
    # Print the result (the emotions detected)
    print(json.dumps(result, indent=4))
