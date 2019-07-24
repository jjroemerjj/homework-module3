
class Player:
    def __init__(self, name: str):
        self.name: str = name
        self.team: str = 'No team'
        self.score: int = 0
        self.value: int = 1

    def description(self):
        des = f"My name is {self.name} and I play in {self.team}. " \
            f"My score is {self.score} and my value is {self.value}"
        return des

    def add_score(self, score):
        self.score += score

    def calculate_value(self):
        self.value = self.score * 10 + 1

    def change_team(self, new_team_name):
        self.team = new_team_name

    def __str__(self) -> str:
        return f"Name: {self.name} Score: {self.score} Value: {self.value}"

