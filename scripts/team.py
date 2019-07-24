
class Team:
    def __init__(self, name: str):
        self.name: str = name
        self.score: int = 0
        self.players: list = []
        self.budget: int = 1000     #this value probably has to be changed (asses Player caclulate.value() method)

    def description(self):
        return f"We are {self.name}, our score is {self.score} and we have budget of {self.budget} PLN"

    def add_player(self, player):
        self.players.append(player)

    def add_score(self, score):
        self.score += score

    def update_budget(self, value):
        self.budget += value


