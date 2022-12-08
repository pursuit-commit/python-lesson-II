class Cat():
    def __init__(self, name, age, color) -> None:
        self.name = name
        self.age = age
        self.color = color
    
    def getName(self): 
        return self.name

    def getAge(self):
        return self.age

    def getColor(self):
        return self.color

    def __str__(self):
        return 'Hi my name is ' + self.name + '... bark!'