from attribute import Attribute
from die import Die
from dice import Dice
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html', message="Roll the Bones")
"""
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
"""

@app.route('/<size>')
def roll(size):
    #try:
    a = Die(size)
    return render_template('index.html', message=a.result, title="Bone Rolled - ")
    #except ValueError as e:
    #    return "Selected endpoint must be int"
@app.route('/coin')
def coin():
    a = Die(2)
    return render_template('index.html', message=a.result, title="Coin Flipped - ")
@app.route('/2d6')
def d6ab():
    a = Die(6)
    b = Die(6)
    together = int(a.result) + int(b.result)

    return render_template('index.html', message=(str(a.result) + " and " + str(b.result) + " | sum = " + str(together)))
@app.route('/character')
def character():
    rolls = Dice(6,4,6)
    attributes = rolls.attributes
    return render_template('character.html', message = "Character Roll", attributes = attributes)
@app.route('/attribute')
@app.route('/trait')
def attribute():
    roll = Attribute()
    return render_template('index.html', message = roll.result)
