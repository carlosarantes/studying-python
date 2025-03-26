x = 25

def printer():
    x = 50
    return x

## --------------

name = 'THIS IS A GLOBAL STRING'

def greet():
    name = 'Sammy' ## LOCAL FUNCTION

    def hello():
        print('Hello '+name)

    hello()

greet()