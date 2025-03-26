## Given a list of ints, return True if the array contains a 3 next to a 3 somewhere
def has_33(list):
    for (index,num) in enumerate(list):
        if num == 3 and index < (len(list) - 1):
            if(list[index+1] == 3):
                return True
        
    return False

print(  has_33([1,3,1,3]) )

print(  has_33([1,4,3,3]) )

## --------  PAPER DOLL: Given a string, return a string where for every character in the original there three characters.
# paper_doll('Hello')

def paper_doll(word):
    new_word = ''
    for letter in word:
        new_word += letter * 3

    return new_word

print(paper_doll('Carlos'))