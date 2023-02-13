from flask import Flask, render_template, request, redirect, url_for
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



@app.route("/users/createForm")
def createUserForm():
    return render_template('newUser.html')

@app.route("/users/create", methods=['POST', 'GET'])
def createUser():
    if request.method=="POST":
        username = request.form['username']
        password = request.form['password']
        fname = request.form['fname']
        lname = request.form['lname']
        # print(username + password + fname + lname)
        conn = openConnection()
        cur = conn.cursor()
        sql = "Insert into `user` (`user_username`, `user_password`, `user_fname`, `user_lname`) values (%s, %s, %s, %s)"
        cur.execute(sql, (username, password, fname, lname))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    else:
        return render_template('newUser.html')


@app.route("/delete/<id>", methods=['GET'])
def delete(id):
    conn = openConnection()
    cur = conn.cursor()
    sql = "DELETE FROM `user` WHERE user_id = %s"
    cur.execute(sql, (id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route("/editForm/<id>", methods=['GET', 'POST'])
def editForm(id):
    conn = openConnection()
    cur = conn.cursor()
    sql = "SELECT * FROM `user` WHERE user_id = %s"
    cur.execute(sql, (id))
    result = cur.fetchall()
    conn.close()
    return render_template('editUser.html', data=result)
    
@app.route("/editForm", methods=['GET', 'POST'])
def edit():
    id = request.form['id']
    username = request.form['username']
    password = request.form['password']
    fname = request.form['fname']
    lname = request.form['lname']
    conn = openConnection()
    cur = conn.cursor()
    sql = "Update `user` set `user_username`=%s, `user_password`=%s, `user_fname`=%s, `user_lname`=%s WHERE user_id = %s"
    cur.execute(sql, (username, password, fname, lname, id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


# Product
@app.route("/product")
def displayProduct():
    conn = openConnection()
    cur = conn.cursor()
    sql = "SELECT * FROM `product`"
    cur.execute(sql)
    result = cur.fetchall()
    conn.close()
    return render_template('product/index.html', datas=result)


# connection.close()
if __name__ == "__main__":
    app.run(debug=True)
