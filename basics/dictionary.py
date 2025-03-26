# KEY : VALUE --- similar to JS objects

my_dict = { 'name': 'Carlos', 'age': 29 }

print(my_dict)

print(my_dict['name'])

products = {
    'apple' : {
        'price': 10.2,
        'quantity': 2
    },
    'banana' : {
        'price': 5.3,
        'quantity': 5
    }
}

print(products)

print(products['apple']['price'])

print(products.keys())

print(products.values())


user = { 'name': 'Andre' }

if 'name' in user:
    print('User has a name...')
else:
    print('User is nameless')