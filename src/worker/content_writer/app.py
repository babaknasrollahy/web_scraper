from flask import Flask,request, jsonify
import mysql.connector

app = Flask(__name__)

def connect_to_database():
    db = mysql.connector.connect(
        host="mysql",
        port="3306",
        user="root",
        password="babak13830",
        database="stack_mag"
    )

content = ""

@app.route('/receive_json/', methods=['GET','POST'])
def receive_text():
    data = request.get_json()
    content = data['name']
    input("are you want to show text??")
    print(f"this is name === {content}")

    print(dict(data))
    return "ok"


@app.route('/content_writer')
def content_writer():
    db = connect_to_database()
    db_cursor = db.cursor()
    wr_cont = ""
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)