from random import randint, choice
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Dice Roller'
@app.route('/d20')
def d20():
    return str(randint(1, 20))
@app.route('/d100')
def d100():
    return str(randint(1, 100))
@app.route('/d4')
def d4():
    return str(randint(1, 4))
@app.route('/d6')
def d6():
    return str(randint(1, 6))
@app.route('/2d6')
def d6ab():
    d6a = randint(1,6)
    d6b = randint(1,6)
    sum = str(d6a + d6b)
    return str(d6a) + " and " + str(d6b) + " (sum: %s)" % sum
@app.route('/d50')
def d50():
    return str(randint(1, 50))
@app.route('/d8')
def d8():
    return str(randint(1, 8))
@app.route('/d10')
def d10():
    return str(randint(1, 10))
@app.route('/coin')
def coin():
    return choice(['heads', 'tails'])
