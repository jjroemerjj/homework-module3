from scripts.database import *
from scripts.player import Player

if __name__ == '__main__':

    """Tutaj importujemy z SQL początkową listę graczy. Następnie na jej podstawie tworzona
    jest lista instancji klasy Player"""
    p_list = get_player_list()
    players = [Player(p[1], p[2], p[3], p[4], p[5]) for p in p_list]
    #[print(row) for row in get_player_list()]







    # print(players[31])
    # print(players[31].value)
    # players[31].add_score(10)
    # players[31].update_database()
    # print(players[31].value)
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
