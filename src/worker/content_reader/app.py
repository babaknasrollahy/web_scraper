
## This app run to get a tag from API and achieve all content of that tag from MYSQL
from flask import Flask
import mysql.connector
import requests
import json

app = Flask(__name__)


########    conneting to the DataBase   #########
def connect_to_database():
    db = mysql.connector.connect(
        host="mysql",
        port="3306",
        user="root",
        password="babak13830",
        database="stack_mag"
    )
    return db
###################################################


@app.route('/<tag>')
def content_reader(tag):
    db = connect_to_database()
    db_cursor = db.cursor()
    read_cont = "select %s AS tag, c.cont_en, c.cont_fa ,i.title,i.writer,i.tags,i.date from contents c JOIN informations i ON c.cont_id = i.cont_id WHERE c.tag_id = (SELECT tag_id from tags WHERE tag = %s) "

    db_cursor.execute(read_cont, (tag,tag))
    result = db_cursor.fetchall()
    for article in result:
        article_json =  {
                            "tag" : article[0],
                            "cont_en" : article[1],
                            "cont_fa" : article[2],
                            "title" : article[3],
                            "writer" : article[4],
                            "tags" : article[5],
                            "date" : str(article[6])
                        }
        headers = {'Content-Type': 'application/json'}
        receiver = "http://api:5000/receive_json/" 
        response = requests.post(receiver, data=json.dumps(article_json), headers=headers)
        # Process the response if needed
        if response.status_code == 200:
            print('Text sent successfully')
        else:
            print('Error sending text')
    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    