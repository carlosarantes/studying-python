# Create a generator that generates the square of numbers up to some number N:

def gensquares(N):
    for x in range(N):
        yield x ** 2 

for x in gensquares(10):
    print(x)

# Create a generator that yields 'n' random numbers between a low and high number (that are inputs).inputNote: use the random library. For example:
    
import random

num = random.randint(1, 10)

def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)

for num in rand_num(1,10,12):
    print(num)

# Use the iter() function to convert the string below into an iterator.
    
s = 'hello'
s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
