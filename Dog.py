class Dog():
    def __init__(self, name, breed, age, color) -> None:
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
    
    def getName(self): 
        return self.name
    
    def getBreed(self):
        return self.breed

    def getAge(self):
        return self.age

    def getColor(self):
        return self.color

    def __str__(self):
        return 'Hi my name is ' + self.name + '... bark!'