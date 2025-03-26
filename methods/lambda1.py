def square(num):
    return num**2

mu_nums = [1,2,3,4,5]

for x in list(map(square, mu_nums)):
    print(x)

## ---------------------------------
    
def slicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]
    

names = ['Andy', 'Eve', 'Sally']

print(list(map(slicer, names)))

## ----------------------------

def check_even(num):
    return num % 2 == 0

my_list_nums = [1,2,3,4,5,6,7,8,9,10]

print(list(filter(check_even, my_list_nums)))

## ----------------------------

squared = lambda num: num ** 2

print(squared(13))


## ----------------------------
list_users = [
    {'name': 'Jorjao Macaxera', 'age': 50}, 
    {'name': 'Claudete Meia-Hora', 'age': -10}, 
    {'name': 'Jubicreuza XupXup', 'age': 80},
    {'name': 'Jorjao Vara-Verde', 'age': 15}
]


print('I need all users called Jorjao: ')
print(list(filter(lambda user: user['name'].find('Jorjao') >= 0, list_users))) 















