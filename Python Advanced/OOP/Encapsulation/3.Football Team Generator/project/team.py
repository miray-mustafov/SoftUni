from project.player import Player


class Team:
    def __init__(self, name, rating: int):
        self.rating = rating
        self.name = name
        self.__players=[]


    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"

        self.__players.append(player)
        return f"Player {player.name} joined team {self.name}"


    def remove_player(self, player_name):
        players_names=[]
        for p in self.__players:
            players_names.append(p.name)
        for i in range(len(players_names)):
            if players_names[i] == player_name:

                return (self.__players.pop(i))

        return f"Player {player_name} not found"


