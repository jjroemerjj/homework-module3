from scripts.database import *

from scripts.player import Player

if __name__ == '__main__':

    [print(row) for row in get_player_list()]
    p_list = get_player_list()






    # team1 = Team('Wisla')
    #
    # player1 = Player("Kuba")
    # player2 = Player("Radek")
    # player3 = Player("Slawek")
    # player4 = Player("Paweł")
    #
    # team1.add_player(player1)
    # team1.add_player(player2)
    # team1.add_player(player3)
    # team1.add_player(player4)
    #
    # team1.show_team()
