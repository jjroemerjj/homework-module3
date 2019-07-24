from scripts.player import Player
from scripts.team import Team

if __name__ == '__main__':

    player1 = Player("Kuba")
    team1 = Team('Wisla')

    print(player1)
    print(team1.description())

    team1.add_player(player1)

    print(type(team1.players))
