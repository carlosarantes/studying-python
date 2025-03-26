class Animal():

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must impletment it")



class Dog(Animal):

    def __init__(self, name):
        Animal.__init__(self, name)
        print('Dog created :) ')

    
    def who_am_i(self):
        print("I am an doog")

    def bark(self):
        print('WOOOOF')

    def __str__(self) :
        return "My dog is crazyyy"
    
    def __len__(self):
        return 1
    
    def __del__(self):
        print("Goodbye my friend")



mydog = Dog('Kaka')

mydog.who_am_i()

print(mydog)

del mydog

print(mydog)
