import random

from flask import Flask
app = Flask(__name__)

answer = random.randint(0, 10)

@app.route('/')
def home():
    return '<h1> Guess a number between 0 and 9 </h1>' \
           '<img src="https://media.giphy.com/media/l378khQxt68syiWJy/giphy.gif">'

@app.route('/<int:number>')
def game(number):
    if number == answer:
        return '<h1 style="color: green">Bullseye! You found it</h1>' \
               '<img src="https://media.giphy.com/media/d3FzOEsc2rwlUKwU/giphy.gif">'
    elif number < answer:
        return '<h1 style="color: red">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/IevhwxTcTgNlaaim73/giphy.gif">'
    else:
        return '<h1 style="color: purple">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/wHB67Zkr63UP7RWJsj/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)