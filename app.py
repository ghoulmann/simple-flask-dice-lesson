from die import Die
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Dice Roller'
@app.route('/d20')
def d20():
    a = Die(20)
    return a.result
@app.route('/d100')
def d100():
    a = Die(100)
    return a.result
@app.route('/d4')
def d4():
    a = Die(4)
    return a.result
@app.route('/d6')
def d6():
    a = Die(6)
    return a.result
@app.route('/2d6')
def d6ab():
    a = Die(6)
    b = Die(6)
    together = int(a.result) + int(b.result)
    return a.result + ", " + b.result + ": " + str(together)
@app.route('/d50')
def d50():
    a = Die(50)
    return a.result
@app.route('/d8')
def d8():
    a = Die(8)
    return a.result
@app.route('/d10')
def d10():
    a = Die(10)
    return a.result
@app.route('/d12')
def d12():
    a = Die(12)
    return a.result
@app.route('/coin')
def coin():
    a = Die(2)
    return a.result