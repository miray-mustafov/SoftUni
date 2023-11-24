class SteamUser:
    def __init__(self, name, games):
        self.games = games
        self.name = name
        self.played_hours = 0

    def play(self,game,hours):
        if game in self.games:
            self.played_hours += hours
            return f"{self.name} is playing {game}"
        else:
            return f"{game} is not in library"

    def buy_game(self, game):
        if game not in self.games:
            self.games.append(game)
            return f"{self.name} bought {game}"
        else:
            return f"{game} already in library"

    def status(self):
        return f"{self.name} has {len(self.games)} games. Total play time: {self.played_hours}"

user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.status())