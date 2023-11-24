class Trainer:
    def __init__(self,name):
        self.name=name
        self.pokemons=[]


    def trainer_data(self):
        result=f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
        for pokemon in self.pokemons:
            result+=f"- {pokemon.details()}\n"
        return result


    def add_pokemon(self,pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.details()}"

        return f"This pokemon is already caught"


    def release_pokemon(self,pokemon_name_torelease):
        for pokemon in self.pokemons:
            if pokemon_name_torelease == pokemon.name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name_torelease}"

        return f"Pokemon is not caught"