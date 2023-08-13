
# get tag from api and check that tag with DataBase and do best work

from flask import Flask 
import mysql.connector
import requests
from datetime import date

###################   Create Conncetion to DataBase   ########################
def connect_to_database():
    db = mysql.connector.connect(
        host="mysql",
        port="3306",
        user="root",
        password="babak13830",
        database="stack_mag"
    )
        
    return db
################################################################################
    
    
app = Flask(__name__)
today = date.today()


###### Checking tag exist or not ######
@app.route('/tag/<tag>')
def test(tag):
    db = connect_to_database()
    db_cursor = db.cursor()
    # sql_qu = "SELECT * FROM contents  WHERE tag_id = (SELECT tag_id FROM tags WHERE tag = %s);"
    sql_qu = "SELECT tag,owner FROM tags WHERE tag = %s "
    ch_result = db_cursor.execute(sql_qu , (tag,))
    ch_result= db_cursor.fetchall()
    
    if ch_result :
        if ch_result[0][1] == "admin": 
            print(f"{tag} tag is alreay exist with admin owner !!")
        else:
            sql_update = "UPDATE tags SET owner = 'admin' WHERE tag = %s " 
            db_cursor.execute(sql_update, (tag,))
            print(f"change owner to admin in tag {tag}")
            db.commit()
            db.close()


        
    else: 
        requests.get(f"http://localhost:5000/add_tag/{tag}")
    
    return "This is the End of Tag_Checker\n"
    

##### Adding tag into Database ######
@app.route('/add_tag/<tag>')
def add_tag(tag):
    db = connect_to_database()
    db_cursor = db.cursor()
    ch_active = "SELECT * FROM tags WHERE status = %s"
    result = db_cursor.execute(ch_active , ("active",))
    result = db_cursor.fetchall()
    
    if result :
        print(f"there is another active tag. {tag} tag add as pending ...")
        add_pending_tag = "INSERT INTO tags(owner,tag,status,date) VALUES('admin', %s , 'pending', %s)"
        db_cursor.execute(add_pending_tag , (tag,today))
        db.commit()
        
    else:
        print(f"ok, {tag} tag is active now ...")  
        add_active_tag = "INSERT INTO tags(owner,tag,status,date) VALUES('admin', %s , 'active', %s)"
        db_cursor.execute(add_active_tag , (tag,today))
        db.commit()
        # requests.get(f"http://link_creator:5000/title/{tag}") ###########
        requests.get(f"http://localhost:5000/send_active/{tag}")
    return "This is the End of add_tag Function\n"
    


# to get tags from bot and write those tags in the DataBase
@app.route('/add_tag_bot/<tag>')
def add_tag_bot(tag):
    db = connect_to_database()
    db_cursor = db.cursor()
    sql_qu = "SELECT tag FROM tags WHERE tag = %s "
    ch_result = db_cursor.execute(sql_qu , (tag,))
    ch_result= db_cursor.fetchall()
    
    if ch_result :
        print(f"{tag} tag is already exit!!")
    
    else: 
        ch_active = "SELECT * FROM tags WHERE status = %s"
        result = db_cursor.execute(ch_active , ("active",))
        result = db_cursor.fetchall()
        if result:
            add_pending_tag = "INSERT INTO tags(owner,tag,status,date) VALUES('bot', %s , 'pending', %s)"
            db_cursor.execute(add_pending_tag , (tag,today))
            db.commit()
        else : 
            add_active_tag = "INSERT INTO tags(owner,tag,status,date) VALUES('bot', %s , 'active', %s)"
            db_cursor.execute(add_active_tag , (tag,today))
            db.commit()
            # requests.get(f"http://link_creator:5000/title/{tag}") ###########
            requests.get(f"http://localhost:5000/send_active/{tag}")
        
        
    


###### Changing active tag ######
@app.route('/complete/')
def set_complete():
    db = connect_to_database()
    db_cursor = db.cursor()
    set_comp = "UPDATE tags SET status = 'completed' WHERE status = 'active'"
    db_cursor.execute(set_comp)
    check_admin = "SELECT tag FROM tags WHERE owner = 'admin' AND status = 'pending' "
    db_cursor.execute(check_admin)
    result = db_cursor.fetchall()
    try:
        if result :
            after_tag = result[0][0]
            change_active = "UPDATE tags SET status = 'active' WHERE tag = %s"
            db_cursor.execute(change_active, (after_tag,))
            db.commit()
            requests.get(f"http://localhost:5000/send_active/{after_tag}")
        
        else:
            check_bot = "SELECT tag FROM tags WHERE owner = 'bot' AND status = 'pending'"
            db_cursor.execute(check_bot)
            result = db_cursor.fetchall()
            after_tag = result[0][0]
            change_active = "UPDATE tags SET status = 'active' WHERE tag = %s"
            db_cursor.execute(change_active, (after_tag,))
            db.commit()
            requests.get(f"http://localhost:5000/send_active/{after_tag}")
    except:
            db.commit()
            print("there is not any pending tag !!!")

        
    return "everyThig is good .\n"

    
    
    
    
@app.route('/send_active/<tag>')
def send_active(tag):
    requests.get(f"http://link_creator:5000/title/{tag}")
    return "Link forwarded to the link_creator\n"



@app.route('/show_active')
def show_active():
    db = connect_to_database()
    db_cursor = db.cursor()
    get_active = "SELECT tag_id,tag FROM tags WHERE status = 'active' "
    db_cursor.execute(get_active)
    result = db_cursor.fetchall()
    return f"{result[0][0]}"  

    
    
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
#INSERT INTO tags(owner,tag,status,date) VALUES('admin', 'python', 'active', '2023-08-08');
#
#INSERT INTO contents(tag_id,cont_en,cont_fa) VALUES(1, 'this is english value' , 'this is farsi value');
#INSERT INTO contents(tag_id,cont_en,cont_fa) VALUES(1, 'this english value' , 'this farsi value');
#
#INSERT INTO informations(cont_id,tag_id,title,date,`like`,writer) VALUES(2,1,'how python works?' , '2023-08-08',50,'babak');