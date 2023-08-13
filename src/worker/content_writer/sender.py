from flask import Flask 
import requests
import json

app = Flask(__name__)

@app.route('/')
def sender_json():
    text = """Unleashing the Power of Quantized Models: A New Era for Generative AI"""


    url = 'http://localhost:5005/receive_json'  # Replace with the URL of the other Flask application's endpoint
    payload = {
                'content': text,
                'name' : 'test',
                'family' : 'testy'
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    # Process the response if needed
    if response.status_code == 200:
        print('Text sent successfully')
    else:
        print('Error sending text')
        
    return("ok")
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)