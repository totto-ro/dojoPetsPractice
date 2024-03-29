class Pet:
    def __init__( self, name, type, tricks ):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 0
        self.energy = 0

    def sleep( self ):
        self.energy += 25
        return self
        

    def eat( self ):
        self.energy += 5
        self.health += 10
        return self
        

    def play( self ):
        self.health += 5
        return self

    def noise( self ):
        print( "woof woof woof!")
        

    def doogieInfo( self ):
        print( f"{self.name} {self.type} {self.tricks}" )
        return self
        