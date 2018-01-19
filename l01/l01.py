class Pokemon:
    """ Handles Pokémons """

    def __init__(self, name, hp, type1, ability1, mass):
        self.name = name
        self.hp =float(hp)
        self.type1 = type1
        self.ability1 = ability1
        self.massStr = mass
        self.massNum = float(mass.split(' ')[0])

    def __str__(self):
        return self.name

    def __lt__(self, other):
        ''' Compares pokémons by mass '''
        try:
            return self.massNum < other.massNum
        except AttributeError:
            return self.massNum < other
        
    def getHp(self) :
        ''' returns hp for pokémon '''
        
        return self.hp
    
    def getHMI(self) :
        '''get helth mass index of the pokemon'''
        
        return self.hp/self.massNum

class Gym:
    """ Manages the pokédexes """

    def __init__(self, pokedex):
        self.pokedex = pokedex

    def __str__(self):
        nameString = ""
        for pkmn in self.pokedex:
            nameString += str(pkmn)
            nameString += " "
        return nameString

    def isMember(self, query):
        ''' Checks if pokémon in query is included in the pokédex '''
        
        memberList = []
        for member in query:
            length = len(memberList)
            for entry in self.pokedex:
                if member.lower() == entry.name.lower():
                    memberList.append(entry.name + " is in the Pokédex")
            if length == len(memberList):
                memberList.append(member + " is not in the Pokédex")
        else:
            return memberList
        
    def printAll(self) :
        ''' Prints all pokémon in the pokédex'''
        
        for pokemon in self.pokedex :
            print (pokemon)
            
    def averageHMI(self) :
        ''' Returns the average health per mass for all pokémon in the pokédex'''
        
        sum = 0
        for pokemon in self.pokedex :
            sum += pokemon.getHMI()
        return sum/len(self.pokedex)
    
    def findByHp(self,hp) :
        ''' Takes hp as input and finds any pokémon in the Pokédex with matching health '''
        
        for pokemon in self.pokedex :
            if pokemon.getHp() == float(hp) :
                print (pokemon)
    
def test():
    """Test function"""

    poke = Pokemon("Bulbasaur", 10, "Fire", "Burn", "10.3 kG")
    poke2 = Pokemon("Pikachu", 10, "Lightning", "Thunder", "4.5 kG")
    if poke < poke2:
        print(poke, "mindre än", poke2)
    print(poke.getHMI())
    print(KTHgym.averageHMI())
    KTHgym.findByHp(90)
    KTHgym.printAll()



def loadPokemons(fileName="pokedex.csv"):
    """ Loads pokémons from a csv file and creates a list of Pokémon objects"""

    pokeList = []
    with open(fileName, encoding="utf-8") as pokedex:
        next(pokedex)  # Skips the indexing line
        for line in pokedex:
            lineList = line.split(",")
            pokeList.append(Pokemon(lineList[2], lineList[3], lineList[10], lineList[13], lineList[16]))
    return pokeList


KTHgym = Gym(loadPokemons())
while True:
    pokemon = input("What Pokémon are You looking for? (For multiple searches, use space to separate the " +
                    "names): ")
    if not pokemon:
        next()
    elif pokemon == "test":
        test()
    else:
        for each in KTHgym.isMember(pokemon.split(" ")):
            print(each)
        break


