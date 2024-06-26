NAME_LIST = ["color", "food", "city", ]
final_result = dict()


def play_game(letter, number_of_players):
    player_dict = dict()

    for player in range(1, number_of_players + 1):
        name_dict = dict()

        for name in NAME_LIST:
            player_input = input(
                f'Player number {player}, Give me your idea about the {name}, which start with "{letter}":'
            )
            name_dict.update({name: player_input})

        player_dict.update({player: name_dict})

    final_result[letter] = player_dict
    return final_result


def compute_scores(result):
    raise NotImplementedError


if __name__ == '__main__':
    number_of_players = int(input("Give me your number of players..."))
    while True:
        letter = input("Give me your letter to play...")
        result = play_game(letter, number_of_players)
        is_end_of_the_game = input("Do you want to finish the game? [Y/N]")
        if is_end_of_the_game.lower() == "y":
            break
    compute_scores(result)
