
# for create api and get "tag" and create "Endpoint"

from flask import Flask
import requests


app = Flask(__name__)


@app.route('/<str:tag>')
def get_tag(tag):
    requests.get(f"http://tag_checker:5000/{tag}")
    return "tag was sended to the link_creator. "



