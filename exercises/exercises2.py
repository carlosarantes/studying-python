## Write a function that computes the volume of a sphere given its radius
## The volume of a sphere is given as: 4/3* PI * radious *** 3

def vol(rad):
    return 4/3*3.14*(rad ** 3)


print(vol(2))

print('-----------------------------------------------')

## ----------------
# Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_bool(num, low, high):
    return num >= low and num <= high

def ran_check(num, low, high):
    if ran_bool(num, low, high):
        print(f'{num} is in the range between {low} and {high}')

ran_check(5,1,5)
##### True

print('-----------------------------------------------')

# Write a Python function that accepts a string and calculates the 
# number of upper case letters and lower case letters.

#### No. of Upper case characters : 4
#### No. of Lower case characters : 33

### Hello Mr. Rogers, how are you this fine Tuesday?

def up_low(text):
    num_of_upper = 0
    num_of_lower = 0

    for letter in text:
        if letter.isupper():
            num_of_upper += 1
        
        if letter.islower():
            num_of_lower += 1

    print(f'No. of Upper case characters: {num_of_upper}')
    print(f'No. of Lower case characters: {num_of_lower}')

 
up_low('Hello Mr. Rogers, how are you this fine Tuesday?')

print('-----------------------------------------------')

# Write a Python function that takes a list and returns a new list with unique elements of the first list

def unique_list(number_list):
    return list(set(number_list))

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

print('-----------------------------------------------')

# Write a python function to miltiply all the numbers in a list:

def multiply_all(numbers):
    result = 1
    for num in numbers:
        result *= num

    return result

print('MULTIPLY ALL PLEASE: {}'.format(multiply_all([1,2,3, -4])))    

print('-----------------------------------------------')

### Write a Python function that checks whether a word or phrase is palindrome or not:

def palindrome(text):
    no_spaces_text = text.replace(' ', '')
    letters = []

    for letter in no_spaces_text:
        letters.append(letter)
    
    letters.reverse()

    return ''.join(letters)



### ---------------------------------------------
   
print('-----------------------------------------------')

import string

def ispangram(text, alphabet=string.ascii_lowercase):
    alphabet_length = len(alphabet)
    letters_set = set()

    for letter in text.lower().replace(' ',''):
         letters_set.add(letter)

    return len(letters_set) == alphabet_length

print(ispangram('The quick brown fox jumps over the lazy dog'))