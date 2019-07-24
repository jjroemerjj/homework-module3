from scripts.player import Player
from scripts.team import Team

if __name__ == '__main__':

    team1 = Team('Wisla')

    player1 = Player("Kuba")
    player2 = Player("Radek")
    player3 = Player("Slawek")

    team1.add_player(player1)
    team1.add_player(player2)
    team1.add_player(player3)

    team1.show_team()
