from flask import Flask, render_template, request
import sqlite3 as sql
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']='sqllight://database.db'

# Initialize DB
db = SQLAlchemy(app)




@app.route('/')
def home():
    return render_template('index.html')

@app.route('/computerlab')
def computerlab():
    return render_template('computer_lab.html')


@app.route('/doe')
def doe():
    return render_template('doe.html')

@app.route('/enternew')
def new_student():
    return render_template('student.html')



@app.route('/doe_pc')
def doe_pc():
    return render_template('doe_pc.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']

            with sql.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO students (name,addr,city,pin) VALUES(?, ?, ?, ?)",(nm,addr,city,pin) )

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html", msg=msg)
            con.close()


@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall()
    return render_template("list.html", rows=rows)


if __name__ == '__main__':
    app.run(debug=True)