from flask import Flask,request
import mysql.connector

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

@app.route('/receive_json/', methods=['GET','POST'])
def receive_text():
    data = request.get_json()
    tag_id = data['tag_id']
    cont_en = data['cont_en']
    cont_fa = data['cont_fa']
    header = data['header']
    date = data['date']
    like = data['like']    
    writer = data['writer']
    other_tags= data['other_tags']
    
    db = connect_to_database()
    db_cursor = db.cursor()

    write_content = "INSERT INTO contents(tag_id,cont_en,cont_fa) VALUES(%s , %s , %s)"
    db_cursor.execute(write_content , (tag_id,cont_en,cont_fa))
    db_cursor.execute("SELECT LAST_INSERT_ID()")
    last_insert_id = db_cursor.fetchall()
    cont_id = last_insert_id[0][0]
    db.commit()
    
    
    write_info = "INSERT INTO informations(cont_id,tag_id,title,`date`,`like`,writer,tags) VALUES(%s, %s, %s, %s, %s, %s, %s)"
    db_cursor.execute(write_info, (cont_id , tag_id, header, date,like,writer,other_tags))
    db.commit()
    print("EveryThing is ok")
    return "ok"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)