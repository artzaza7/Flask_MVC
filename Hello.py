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
    dataIs = 5
    return render_template('index.html', data = dataIs)

@app.route("/students")
def studentRoute():
    return "Hello Student!"

if __name__ == "__main__":
    app.run(debug=True)