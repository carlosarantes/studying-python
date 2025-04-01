def hello(name='Jose'):
    print('The hello() function has been executed!')

    def greet():
        return '\t This is the greet() func inside hello!'
    
    def welcome():
        return '\t This is welcome() inside hello'
    
    print("I will return a function!!")

    if name == 'Jose':
        return greet
    else:
        return welcome
    
test = hello('Mary')
print(test())


def cool():
    def super_cool():
        return "I am very cool"
    
    return super_cool



def hello2():
    return "Hi Jose"

def other_func(some_func):
    print('Other code runs here..')
    print(some_func())

other_func(hello2)

### ------------------
### ------------------

def new_decorator(original_func):

    def wrap_func():
        print("Some extra code, before the original function")
        original_func()
        print("Some extra code, after the original function!")
    
    return wrap_func


def func_needs_decorator():
    print("I want the decorator")


decorated_func = new_decorator(func_needs_decorator)

decorated_func()


### ------------------
### ------------------

print('---------------------------------')

@new_decorator
def func_needs_decorator():
    print('I want to be decorated!')

func_needs_decorator()

### -----------------------------------------
### -----------------------------------------
