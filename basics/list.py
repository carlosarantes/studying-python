my_list = [1,2,3]

other_lists = ['STRING', 100, 23.2]

print(len(other_lists))

other_other_list = ['one', 'two']

other_other_list[0]

another_one = my_list + other_other_list


another_one[0] = 'new'
print(another_one)


another_one.append('teste')

print(another_one)

print(another_one.pop())

print(another_one)


print(another_one.pop(3)) ## IT ALSO ACCEPTS index to be removed


## SORTING...

list1 = [ 'b', 'a', 'f', 'h', 'z', 'd' ]

list2 = [4,8,9,2,3,1]


list2.sort()

print(list2)

list2.reverse()

## ---------------------------------



mylist2 = [1,2,3,4]
mylist3 = ['a','b','c','d']

tup = zip(mylist2, mylist3)
print('Tup ??')
print(tup)

for item in tup:
    print(item)

print(list(tup))

if 3 in mylist2:
    print('PARABENS VOCE GANHOU ...')

### SOME OPTIMIZATIONS
    
mylistofstr = [letter for letter in 'abcdefgg']

print(mylistofstr)

# ----------------------------

mylistnums1 = [num**2 for num in range(0,11)]
print(mylistnums1)

# ----------------------------


mylistnums2 = [num**2 for num in range(0,11) if num%2 == 0]
print(mylistnums2)
