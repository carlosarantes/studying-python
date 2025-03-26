class Dog():

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

    def bark(self):
        print(f'WOOOF! My name is {self.name}')

animal = Dog(breed='Lab',name='Xupxup',spots='NO SPOTS')