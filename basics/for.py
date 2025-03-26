my_iterable = [1,2,3,4]

for item in my_iterable:
    print(item)

print('\n')

for letter in 'Lieben Benutzer':
    print(letter)

my_tuple = (1,3,5,7,9,11,13,15,17,19)

for item in my_tuple:
    print(f'Item inside my tup: {item} ...')

## ----------------------
    
list_tuples = [(10,20,30),(40,50,60),(70,80,90),(100,110,120)]

for (a,b,c) in list_tuples:
    print(f'item A: {a}')
    print(f'item B: {b}')
    print(f'item C: {c}')


d = { 'k1': 1, 'k2': 2, 'k3': 3 }

for value in d.values():
    print(value)


## --------------
    
mylist = [1,2,3]

for num in list(range(2,10,2)):
    print(f'Das nummer ist {num}')

## --------------

index_count = 0
word = 'abcde'

for (index, item) in enumerate(word):
    print(f'Letter in {index} is ... {item}')


## --- NESTED LOOPS
    
myotherlistnums = []

for x in [2,4,6]:
    for y in [100, 200, 300]:
        myotherlistnums.append(x * y)

print(myotherlistnums)


## ----------------------

nestlooplist = [x*y for x in [2,4,6] for y in [100,200,300]]

print(nestlooplist)