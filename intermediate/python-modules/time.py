import time

def func_one(n):
    return list(map(str, range(n)))

start_time = time.time()

result =  func_one(100000)

end_time = time.time()

elapsed_time = end_time - start_time

print(elapsed_time)

### ---------------------

import timeit

stmt = '''
func_one(100000)
'''

setup = '''
def func_one(n):
    return list(map(str, range(n)))
'''

print(timeit.timeit(stmt, setup, number=1000))

## --------------------------------------------






