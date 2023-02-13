from flask import Flask, render_template
import pymysql

app = Flask(__name__)


# connection Database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='flaskdb_test',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
# localhost, username, password, database


@app.route("/")
def hello():
    with connection:
        cur = connection.cursor()
        cur.execute("SELECT * FROM `user`")
        rows=cur.fetchall()
        return render_template('index.html', datas=rows)

@app.route("/students")
def studentRoute():
    return "Hello Student!"

if __name__ == "__main__":
    app.run(debug=True)