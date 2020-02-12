from flask_sqlalchemy import SQLAlchemy
#from datetime import timestamp
from die import Die
#from models import Die
from flask import Flask, render_template
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Roll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer, unique=False, nullable=False)
    size = db.Column(db.Integer, unique=True, nullable=False)
    timestamp = db.Column(db.DateTime(timezone=False), unique=False, nullable=False)
    def __repr__(self):
        return '<Roll %r>' % self.timestamp

@app.route('/')
def hello_world():
    return render_template('index.html', message="Roll 'Bones")

@app.route('/<size>')
def roll(size):
    a = Die(size)
    return render_template('index.html', message=a.result, title="Bone Rolled")
@app.route('/coin')
def coin():
    a = Die(2)
    return render_template('index.html', message=a.result, title="Coin Flipped")
@app.route('/2d6')
def d6ab():
    a = Die(6)
    b = Die(6)
    together = int(a.result) + int(b.result)
    return render_template('index.html', message=(str(a.result) + " and " + str(b.result) + " | sum = " + str(together)))
