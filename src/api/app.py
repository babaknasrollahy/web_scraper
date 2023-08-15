
# for create api and get "tag" and create "Endpoint"

from flask import Flask,request
import requests


app = Flask(__name__)

# get a tag and send it to tag_checker
@app.route('/<tag>')
def get_tag(tag):
    requests.get(f"http://tag_checker:5000/tag/{tag}")
    return "tag was sent to the tag_checker.\n "



# get a tag and read setd it to the content_reader to achive all articles in the DataBase
@app.route('/get_data/<tag>')
def get_data(tag):
    # requests.get(f"http://content_reader:5005/{tag}") 
    requests.get(f"http://content_reader:5000/{tag}") 
    return "tag was sent to the content_reader.\n "


# recive json from content_reader and send that to the EndPoint
@app.route('/receive_json/', methods=['GET','POST'])
def receive_json():
    data = request.get_json()
    print(f"{data}\n\n\n")
    
    return "ok"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)



