def create_cubes(n):
     for x in range(n):
        yield x**3

## -------------------------------

def gen_fibon(n):
    a = 1
    b = 1

    for i in range(n):
        yield a
        a,b = b,a + b

for number in gen_fibon(10):
    print(number)

## -------------------------------

def simple_gen():
    for x in range(3):
        yield x  

for number in simple_gen():
    print(number)

## -------------------------------

s = 'hello'

s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))

