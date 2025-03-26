def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

row1 = [ ' ', ' ', ' ' ]
row2 = [ ' ', ' ', ' ' ]
row3 = [ ' ', ' ', ' ' ]

row2[1] = 'x'

display(row1, row2, row3)

def user_choice():
    choice = 'x'

    while choice.isdigit() == False or int(choice) not in range(0, 10):
        choice = input("Please enter a number (0-10): ")
    
    return int(choice)

result = user_choice()
