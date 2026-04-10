import json
import requests


def analyze_emotions(fmt):
    # extract emotions
    predictions_array = fmt["emotionPredictions"]
    predictions = predictions_array[0]
    emotions = predictions["emotion"]

    # initialize collector
    maximum = 0
    dominant_emotion = ''

    # find top scorer by iterating over key, val
    for emotion, score in emotions.items():
        if score > maximum:
            maximum = score
            dominant_emotion = emotion

    # add dominant_emotion and return the dict
    emotions['dominant_emotion'] = dominant_emotion
    return emotions


def emotion_detector(text_to_analyze):

    # URL of the emotion_detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header, timeout=1000)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    print(formatted_response)

    # Extracting emotions and calculate the dominant emotion
    response_emotions = analyze_emotions(formatted_response)

    # Write response to a text file
    output_text = json.dumps(response_emotions, sort_keys=False, indent=4)
    with open('3a_output_formatting', 'w', encoding='UTF-8') as outfile:
        outfile.write(output_text)

    # Return the response text from the API
    return response_emotions

if __name__ == '__main__':
    emotion_detector('')
