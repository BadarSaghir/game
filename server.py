from flask import Flask
import random

app = Flask(__name__)
random_: int = 0


@app.route('/')
def random_gif():
    global random_
    random_ = random.randrange(1, 10)
    return '<h1>Guess a number 0 to 9</h1>' \
           '<img src = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"/>'


@app.route('/<guess>')
def random_number(guess):
    guess = int(guess)
    if guess == random_:
        return '<h1>You found me</h1>' \
               '<img src = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>'
    elif guess > random_:
        return '<h1>Too High! try again</h1>' \
               '<img src = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"/>'
    else:
        return '<h1>Too Low! Try again</h1>' \
               '<img src = " https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"/>'


if __name__ == '__main__':
    app.run(debug=True)
