# Handle the exception thrown by the code below by using try and except blocks
try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except:
    print('Something happened')

# Handle the exception thrwon by the code below by using try and except blocks. then use a finally block to print 'All Done' 
try:
    x = 5
    y = 0

    z = x/y
except:
    print("Some error occurred...")
finally:
    print("All Done.")

# Write a function that asks for an integer and prints the square of it. Use a while loop with a try / except , else block to account for incorrect input.input
    
def ask():

    while True:
        try:
            num = int(input('Input an integer: '))
        except:
            print("An error occured! Please try again!")
        else:
            print(f'Thank you, your number squared is: {num**2}')
            break

ask()