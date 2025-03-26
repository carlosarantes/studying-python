def myfunc(*args): ## args will set as TUPLE
    return sum(args) * 0.05

print(myfunc(20,40,60,80,100))

def otherfunc(**kwargs): ## set as a DICTIONARY
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))


otherfunc(test='cerveja', fruit='mango')

print('-------------------------------------------')

def myfunc(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))


myfunc(33,1,2,3,5,4,5, food='fries and chicken', juice='orange' )


print('-------------------------------------------')

def minimun_num(*args):
    return min(args) # there is also max(...)

print(minimun_num(-3,2,3,4,5,6,7,8,9))

print('-------------------------------------------')

def old_macdonalds(name):
    first_half = name[:3]
    second_half = name[3:]

    return first_half.capitalize() + second_half.capitalize()

print(old_macdonalds('macdonalds'))

print('-------------------------------------------')

def master_yoda(text):
    words = text.split()
    words.reverse()
    return ' '.join(words)





print(master_yoda('EU sou foda pra caraio'))
