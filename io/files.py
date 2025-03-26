my_file = open('test.txt')

print(my_file.read())

my_file.seek(0)

print(my_file.read())

## --------------------------------

my_file.seek(0)

print(my_file.readlines())

my_file.close()

## *****************************

with open('test.txt') as my_new_file:
    content = my_new_file.read()
    print(content)

## *****************************

with open('test.txt', mode='a') as my_new_file:
    my_new_file.write('\nMY NEW LINE')
