class Pet():
    def init(self, name, age) -> None:
        self.name = name
        self.age = age

    # When imagining what a parent class should have, think about what all of its children will have in common
    # Properties that are common to all pets are name and age
    # Methods that are common to all pets are getName, getAge, and __str__
    # implement those methods below

    def __str__(self):
        return 'Hi my name is ' + self.name