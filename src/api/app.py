
# for create api and get "tag" and create "Endpoint"

from flask import Flask
import requests


app = Flask(__name__)


@app.route('/<tag>')
def get_tag(tag):
    requests.get(f"http://tag_checker:5000/tag/{tag}")
    return "tag was sended to the tag_checker. "

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)



