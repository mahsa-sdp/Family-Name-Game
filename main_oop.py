class Game:
    NAME_LIST = ["color", "food", "city"]

    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.final_result = {}

    def play_round(self, letter):
        player_dict = {}

        for player in range(1, self.number_of_players + 1):
            name_dict = {}

            for name in self.NAME_LIST:
                player_input = input(
                    f'Player number {player}, Give me your idea about the {name}, which starts with "{letter}":'
                )
                name_dict[name] = player_input

            player_dict[player] = name_dict

        self.final_result[letter] = player_dict

    def play_game(self):
        while True:
            letter = input("Give me your letter to play...")
            self.play_round(letter)
            is_end_of_the_game = input("Do you want to finish the game? [Y/N]")
            if is_end_of_the_game.lower() == "y":
                break

    def compute_scores(self):
        raise NotImplementedError


if __name__ == '__main__':
    number_of_players = int(input("Give me your number of players..."))
    game = Game(number_of_players)
    game.play_game()
    game.compute_scores()
