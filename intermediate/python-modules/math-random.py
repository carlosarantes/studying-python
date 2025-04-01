import math

value = 4.35

print(math.floor(value))

print(math.ceil(value))

print(round(value))

print(math.pi)

print(math.inf)

print(math.nan)

print(math.log(math.e))

math.log(100, 10)

math.sin(10)

## --------------------------------------

import random

random.seed(101)

random.randint(0, 100)

print(random.choice( range(1, 200) ))

random.choices(population=list(range(1,200)), k=10)