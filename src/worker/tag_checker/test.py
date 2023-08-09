from flask import Flask
import mysql.connector

app = Flask(__name__)

def connect_to_database():
    db = mysql.connector.connect(
        host="127.0.0.1",
        port="6603",
        user="root",
        password="babak13830",
        database="stack_mag"
    )
        
    return db

@app.route('/complete/')
def set_complete():
    db = connect_to_database()
    db_cursor = db.cursor()
    set_comp = "UPDATE tags SET status = 'completed' WHERE status = 'active'"
    db_cursor.execute(set_comp)
    check_admin = "SELECT tag FROM tags WHERE owner = 'admin' AND status = 'pending' "
    db_cursor.execute(check_admin)
    result = db_cursor.fetchall()
    print(result)
    try:
        if result :
            after_tag = result[0][0]
            print(after_tag)
            change_active = "UPDATE tags SET status = 'active' WHERE tag = %s"
            db_cursor.execute(change_active, (after_tag,))
            db.commit()
        
        else:
            check_bot = "SELECT tag FROM tags WHERE owner = 'bot' AND status = 'pending'"
            db_cursor.execute(check_bot)
            result = db_cursor.fetchall()
            after_tag = result[0][0]
            change_active = "UPDATE tags SET status = 'active' WHERE tag = %s"
            db_cursor.execute(change_active, (after_tag,))
            db.commit()
    except:
            db.commit()
            print("there is not any pending tag !!!")

        
    return "everyThig is good .\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)