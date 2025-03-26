my_dogs = 2

print(type(my_dogs))


result = 100/777

## FLOATING PRECISION

print("My result was {q:1.3f}".format(q=result))


## -------------------------------------


list_numbers = [10,20,30,40,50,60,70,80,90,100]
print(min(list_numbers))

print(max(list_numbers))

from random import shuffle, randint

shuffle(list_numbers)

print(list_numbers)

print(randint(0,1000))

## ------------------------------

result = input(f'Enter a number for {'USER'}:')
print(int(result)) ## CAST TO INT