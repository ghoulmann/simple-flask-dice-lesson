from die import Die
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Dice Roller'
@app.route('/d20')
def d20():
    a = Die(20)
    return a.roll
@app.route('/d100')
def d100():
    a = Die(100)
    return a.roll
@app.route('/d4')
def d4():
    a = Die(4)
    return a.roll
@app.route('/d6')
def d6():
    a = Die(6)
    return a.roll
@app.route('/2d6')
def d6ab():
    a = Die(6)
    b = Die(6)
    return a.roll + ", " + b.roll
@app.route('/d50')
def d50():
    a = Die(50)
    return a.roll
@app.route('/d8')
def d8():
    a = Die(8)
    return a.roll
@app.route('/d10')
def d10():
    a = Die(10)
    return a.roll
