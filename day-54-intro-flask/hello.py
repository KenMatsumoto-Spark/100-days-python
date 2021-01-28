from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def wrapper(*args, **kwargs):
        return f"<b>{function()}</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center"> Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media.giphy.com/media/YxA2PPkXbwRTa/giphy.gif" width=200>'

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Bye!'

@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)

#----------------------------------------------
# Create the logging_decorator() function 👇
print()
def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")
        print(f"It returned {function(*args)}")
    return wrapper

# Use the decorator 👇

@logging_decorator
def a_function(a, b, c):
    return a*b*c

a_function(1, 2, 3)