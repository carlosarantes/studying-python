# Use for, .split(), and if to create a Statement that will print out words that start with 's' :
print('Exercise 1: \n')
phrase = 'HI, today is sunny summer there is no snow, I want a strewberry icecream please, sort it...'

for word in phrase.split():
    if word[0].lower() == 's':
        print(word)

# Use range() to print all the even numbers from 0 to 10.
print('--------------------------------------')
print('Exercise 2: \n')

for num in range(0, 11):
    if num %2 == 0 and num > 0:
        print(f'Num {num} is even :)')

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3:
print('--------------------------------------')
print('Exercise 3: \n')

divisible_three_list = [num for num in range(1, 51) if num % 3 == 0]
print(divisible_three_list)

# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'

for (index, word) in enumerate(st.split()):
    if len(word) % 2 == 0:
        print(f'Word {word} at index {index} - even!')

# Write a program that prints the integers from 1 to 100. But for multiples of three print
# "Fizz" instead of number, and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
print('--------------------------------------')
print('Exercise 4: \n')

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

# Use List Comprehension to create a list of the first letters of every word in the string below.
print('--------------------------------------')
print('Exercise 5: \n')

st = 'Create a list of the first letters of every word in this string'

list_first_letters = [word[0] for word in st.split()]

print(list_first_letters)
