from Dog import Dog
from Cat import Cat

class AdoptionAgency():
    def __init__(self) -> None:
        self.dogs: list[Dog] = []
        self.cats: list[Cat] = []

    def addDog(self, dog: Dog):
        # add a property called dateArrived
        self.dogs.append(dog)
    
    def addCat(self, cat: Cat):
        # add a property called dateArrived
        self.cats.append(cat)

    def getDogsByBreed(self, breed: str) -> list[Dog]:
        pass

    def getCatsByColor(self, color: str) -> list[Cat]:
        pass

    def getAllPuppies(self) -> list[Dog]:
        pass

    def getAllKittens(self) -> list[Cat]:
        pass

    def getOldestDog(self) -> Dog:
        pass

    def getOldestCat(self) -> Cat:
        pass