class Pokemon:
    def __init__(self, name, level, type, max_health, cur_health, isKO):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = max_health
        self.cur_health = cur_health
        self.isKO = isKO
        if self.level == 1:
            self.max_health = 25
        elif self.level == 2:
            self.max_health = 50
        elif self.level == 3:
            self.max_health = 100

    def __repr__(self):
        # Printing a pokemon will tell you its name, its type, its level and how much health it has remaining
        return "This level {level} {name} has {health} hit points remaining. They are a {type} type Pokemon".format(level = self.level, name = self.name, health = self.cur_health, type = self.type)
        

    def knock_out(self):
        if self.cur_health == 0:
            self.isKO = True
            print("{} is unable to battle.".format(self.name))


    def lose_health(self, damage):
        self.cur_health -= damage
        if self.cur_health <= 0:
            #Makes sure the health doesn't become negative. Knocks out the pokemon.
            self.cur_health = 0
            self.knock_out()
        else:
            print("{} now has {} health".format(self.name, self.cur_health))
   
    def regain_health(self, amount):
        #Adds to a Pokemon's health
        #If a Pokemon goes from 0 health, then revive it
        if self.cur_health == 0:
            self.revive()
        self.cur_health += amount
        #Makes sure the health does not go over the max health
        if self.cur_health >= self.max_health:
            self.cur_health = self.max_health
        print("{name} now has {health} health.".format(name = self.name, health = self.cur_health))
        
    
    def revive(self):
        if self.isKO == True:
            self.cur_health = 1
            self.isKO = False
            print("{} has been revived and has {} health".format(self.name, self.cur_health))
    

    def attack(self, pokemon_obj):

        #Edge Case
        if self.isKO:
            print("{} is unable to battle, {} wins!".format(self.name, pokemon_obj.name))
            return

        if self.type == 'Fire' and pokemon_obj.type == 'Grass':
            hit = 2 * self.level
            print("{} attacked {}".format(self.name, pokemon_obj.name))
            pokemon_obj.lose_health(hit)
        elif self.type == 'Fire' and pokemon_obj.type == 'Water':
            hit = self.level * 0.5
            pokemon_obj.cur_health -= hit
            print("{} attacked {}".format(self.name, pokemon_obj.name))
            pokemon_obj.lose_health(hit)
        elif self.type == 'Fire' and pokemon_obj.type == 'Fire':
            hit = self.level
            pokemon_obj.cur_health -= hit
            print("{} attacked {}".format(self.name, pokemon_obj.name))
            pokemon_obj.lose_health(hit)

        if self.type == 'Water' and pokemon_obj.type == 'Fire':
            hit = 2 * self.level
            pokemon_obj.cur_health -= hit
            print("{} attacked {}".format(self.name, pokemon_obj.name))
            pokemon_obj.lose_health(hit)
        elif self.type == 'Water' and pokemon_obj.type == 'Grass':
            hit = self.level * 0.5
            pokemon_obj.cur_health -= hit
            print("{} attacked {}".format(self.name, pokemon_obj.name))
            pokemon_obj.lose_health(hit)
        elif self.type == 'Water' and pokemon_obj.type == 'Water':
            hit = self.level
            pokemon_obj.cur_health -= hit
            print("{} attacked {}".format(self.name, pokemon_obj.name))
            pokemon_obj.lose_health(hit)

        if self.type == 'Grass' and pokemon_obj.type == 'Water':
            hit = 2 * self.level
            pokemon_obj.cur_health -= hit
            print("{} attacked {}".format(self.name, pokemon_obj.name))
            pokemon_obj.lose_health(hit)
        elif self.type == 'Grass' and pokemon_obj.type == 'Fire':
            hit = self.level * 0.5
            pokemon_obj.cur_health -= hit
            print("{} attacked {}".format(self.name, pokemon_obj.name))
            pokemon_obj.lose_health(hit)
        elif self.type == 'Grass' and pokemon_obj.type == 'Grass':
            hit = self.level
            pokemon_obj.cur_health -= hit
            print("{} attacked {}".format(self.name, pokemon_obj.name))
            pokemon_obj.lose_health(hit)


# Three classes that are subclasses of Pokemon. Charmander is a fire type, Squirtle is a Water type, and Bulbasaur is a Grass type.
class Charmander(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Charmander", "Fire", level)

class Squirtle(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Squirtle", "Water", level)

class Bulbasaur(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Bulbasaur", "Grass", level)


class Trainer():
    def __init__(self, pokemons, name, num_potions, cur_pokemon):
        self.pokemons = pokemons
        self.name = name
        self.num_potions = num_potions
        self.cur_pokemon = cur_pokemon
        

    def __repr__(self):
        #Prints the name of the trainer, the Pokemonm they currently have, and the current active pokemon
        print("The trainer {name} has the following pokemon".format(name = self.name))
        for pokemon in self.pokemons:
            print(pokemon.name)
        return "The current active pokemon is {name}".format(name = self.pokemons[self.cur_pokemon].name)


    def use_potion(self):
        self.revive(self.cur_pokemon) #heals 20 health


    def attack_another_trainer(self, other_trainer):
        # self.cur_pokemon.attack(another_trainer.cur_pokemon)
        # "{}\'s {} attacked {}\'s {}".format(self.name, self.cur_pokemon.name, another_trainer.name, another_trainer.cur_pokemon.name)
        #Edge Case
        # if ((self.pokemons[self.cur_pokemon]).isKO == True):
        #     print("{} is unable to battle, {} wins!".format(self.pokemons[self.cur_pokemon]), other_trainer.pokemons[other_trainer.cur_pokemon])
        #     return

        their_pokemon = other_trainer.pokemons[other_trainer.cur_pokemon]
        (self.pokemons[self.cur_pokemon]).attack(their_pokemon)


    def cur_active_pokemon(self, new_active):
        #Switches the active pokemon to the number given as a parameter
        #First checks to see the number is valid (between 0 and the length of the list)
        if new_active < len(self.pokemons) and new_active >= 0:
            #You can't switch to a Pokemon that is knocked out
            if self.pokemons[new_active].isKO:
                print("{name} is knocked out. You can't make it your active Pokemon".format(name = self.pokemons[self.cur_pokemon].name))
            # You can't switch to your current pokemon
            elif new_active == self.cur_pokemon:
                print("{name} is already your active pokemon".format(name = self.pokemons[new_active].name))
            # Switches the pokemon
            else:
                self.cur_pokemon = new_active
                print("Go {name}, it's your turn!".format(name = self.pokemons[self.cur_pokemon].name))
                
        # #Edge Case
        # if ((self.pokemons[self.cur_pokemon]).isKO == True):
        #     print("{} is unable to battle, {} wins!".format(self.pokemons[self.cur_pokemon]), other_trainer.pokemons[other_trainer.cur_pokemon])
        #     return
        # self.cur_pokemon = pokemon
        # print("{} is now the current active Pokemon".format(pokemon.name))



p1 = Pokemon("Charizard", 3, "Fire", 100, 100, False)
p2 = Pokemon("Venusaur", 3, "Grass", 100, 100, False)
p3 = Pokemon("Blaziken", 3, "Fire", 100, 100, False)
p4 = Pokemon("Chikorita", 1, "Grass", 25, 25, False)
p5 = Pokemon("Greninja", 3, "Water", 100, 100, False)
p6 = Pokemon("Torterra", 3, "Grass", 100, 100, False)

p7 = Pokemon("Bulbasaur", 1, "Grass", 25, 25, False)
p8 = Pokemon("Flareon", 2, "Fire", 50, 50, False)
p9 = Pokemon("Infernape", 3, "Fire", 100, 100, False)
p10 = Pokemon("Oshawott", 1, "Water", 25, 25, False)
p11 = Pokemon("Empoleon", 3, "Water", 100, 100, False)
p12 = Pokemon("Grovyle", 2, "Grass", 50, 50, False)


print(p1)
print(p11)

# print(p1.cur_health)
# print(p2.cur_health)
# p1.attack(p2)
# print(p1.cur_health)
# print(p2.cur_health)

party1 = [p1, p2, p3, p4, p5, p6]
party2 = [p7, p8, p9, p10, p11, p12]

t1 = Trainer(party1, "Ash", 6, 0)   
t2 = Trainer(party2, "Paul", 6, 4)  


print(t1) #The current active pokemon is Charizard
print(t2) #The current active pokemon is Empoleon

t1.attack_another_trainer(t2)


p1.lose_health(100)
p11.lose_health(100)

print(p1.cur_health)
print(p11.cur_health)


t1.cur_active_pokemon(1)
t2.cur_active_pokemon(2)
