from flask import Flask, render_template
import pymysql

app = Flask(__name__)


# connection Database
def openConnection():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 database='flaskdb_test',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection
# localhost, username, password, database


@app.route("/")
def index():
    conn = openConnection()
    cur = conn.cursor()
    sql = "SELECT * FROM `user`"
    cur.execute(sql)
    result = cur.fetchall()
    conn.close()
    return render_template('index.html', datas=result)



@app.route("/users/create")
def createUserForm():
    return render_template('newUser.html')


# connection.close()
if __name__ == "__main__":
    app.run(debug=True)
