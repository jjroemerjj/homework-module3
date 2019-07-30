from scripts.database import *


class Player:
    def __init__(self, name: str, team: str = 'No team', position: str = 'No position',
                 score: int = 0, value: int = 1):
        self.name: str = name
        self.team: str = team
        self.position: str = position
        self.score: int = score
        self.value: int = value

    def description(self) -> str:
        des = f"My name is {self.name} and I play in {self.team}. " \
            f"My score is {self.score} and my value is {self.value}"
        return des

    def update_database(self) -> None:
        update_players_database(self.name, self.team, self.score, self.value)




    # def add_score(self, score):
    #     self.score += score
    #
    # def calculate_value(self):
    #     self.value = self.score * 10 + 1
    #
    # def change_team(self, new_team_name):
    #     self.team = new_team_name

    def __str__(self) -> str:
        return f"Name: {self.name} Score: {self.score} Value: {self.value}"

