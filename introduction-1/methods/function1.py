def my_first_function():
    print('CORNO')

my_first_function()

def second_function(dic : dict = { 'test' : 'value'  }):
    print(dic)

def with_return() :
    return 13

second_function({ 'test': 'a' })

second_function()

print(with_return())

## ------------

def is_even(num):
    return num % 2 == 0

def some_is_even(num_list = [1,2,3]):
    has_even = False
    for num in num_list:
        if num % 2 == 0:
            has_even = True 
            break
    return has_even


def other_even_check(num_list):
    has_even = False
    curr_index = 0

    while curr_index < len(num_list) and has_even == False :
        has_even = num_list[curr_index] % 2 == 0
        curr_index += 1
    return has_even

def odd_number_check(num_list):
    for num in num_list:
        if num % 2 != 0:
            return True
        else:
            pass

print(some_is_even([1,2,3]))

print(other_even_check([1,2,3]))

print(odd_number_check([4,2,6,5]))