from collections import Counter

mylist = [1,1,1,1,2,2,2,2,3,3,3,3,3,3]

print(Counter(mylist))

sentence = 'How many times does each word word show up in this sentence'

print( Counter(sentence.split()) )

c = Counter(sentence.split())
print('--------------------')
print(c.most_common())

from collections import defaultdict

d = { 'a': 10 }

d = defaultdict(lambda : 0)

print( d['TEST'] )

## ---------------------------

mytuple = (10,20,30)

from collections import namedtuple

Dog = namedtuple('Dog', ['age', 'breed', 'name'])

sammy = Dog(name='Sammy', breed='Lab', age=5)

print(sammy)


## ---------------------------


