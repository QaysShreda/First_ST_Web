from flask_sqlalchemy import SQLAlchemy
import sqlite3
from flask import Flask, render_template, request,redirect


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

class Computers(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    brand = db.Column(db.String(50))

    def __repr__(self):
        return '<brand %r>' % self.id

@app.route('/', methods =['POST','GET'])
def computers():
    if request.method == "POST":
        brand = request.form['brand']
        new_computers = Computers(brand = brand)

        try:
            db.session.add(new_computers)
            db.session.commit()
            return redirect('/')
        except:
            return db.error
    else:
        comp = Computers.query.order_by(Computers.id)
        return render_template("computers.html",comp = comp)

if __name__ == '__main__':
    app.run()