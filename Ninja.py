

class Ninja:
    def __init__( self, firstName, lastName, treats, petFood, pet ):
        self.firstName = firstName
        self.lastName = lastName
        self.treats = treats
        self.petFood = petFood
        self.pet = pet
        
    def walk( self ):
        self.pet.play()
        return self

    def feed( self):
        self.pet.eat()
        return self

    def bathe( self):
        self.pet.noise()
        return self

    def printInfo( self ):
        print( f"Owner: {self.firstName} {self.lastName}, Treats: {self.treats}, Dog food: {self.petFood}" )
        self.pet.doogieInfo()
        self.pet.noise()
        self.pet.sleep()
        
