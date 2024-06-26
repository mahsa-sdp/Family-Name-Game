def init():
    number_of_players = int(input("Give me your number of players..."))
    first_letter = input("Give me your letter to play...")
    return number_of_players, first_letter


class User:
    def __init__(self, id):
        self.id = id
        self.choices = dict()


class Game:
    __questions = ["color", "food", "city", "animal"]

    def __init__(self, number_of_players, first_letter):
        self.number_of_players = number_of_players
        self.letters = [first_letter, ]
        self.current_letter = first_letter
        self.players = [User(i) for i in range(1, self.number_of_players + 1)]
        self.score = Score(self.players, self.letters, self.__questions)

    def play_round(self):
        for player in self.players:
            answers_dict = dict()
            for question in self.__questions:
                player_input = input(
                    f'Player number {player.id}, Give me your idea about the {question}, '
                    f'which starts with "{self.current_letter}":'
                )
                answers_dict[question] = player_input

            player.choices[self.current_letter] = answers_dict

    def is_end_of_the_game(self):
        return input("Do you want to finish the game? [Y/N]").lower()

    def play_game(self):
        while True:
            self.play_round()
            is_end = self.is_end_of_the_game()
            while is_end not in ["y", "n"]:
                print('Unknown command! Give me just "y" or "n".')
                is_end = self.is_end_of_the_game()

            if is_end == "y":
                break
            elif is_end == "n":
                self.letters.append(input("Give me your letter to play..."))
                self.current_letter = self.letters[-1]


class Score:
    def __init__(self, players, letters, questions):
        self.players = players
        self.letters = letters
        self.questions = questions

    def process_list(self, target_char, input_list):
        count_dict = {}
        for item in input_list:
            if item:
                count_dict[item] = count_dict.get(item, 0) + 1
        output_list = []
        for item in input_list:
            if item == '':
                output_list.append(0)
            elif item.startswith(target_char):
                if count_dict[item] > 1:
                    output_list.append(5)
                else:
                    output_list.append(10)
            else:
                output_list.append(0)
        return output_list

    def find_winner(self, matrix):
        sums = [0] * len(matrix[0])
        for row in matrix:
            for idx, value in enumerate(row):
                sums[idx] += value
        max_sum = max(sums)
        winning_indices = [i for i, s in enumerate(sums) if s == max_sum]
        return winning_indices, sums

    def compute_scores(self):
        result_dict = {key: {nested_key: [] for nested_key in self.questions} for key in self.letters}
        for letter in self.letters:
            for player in self.players:
                dict_ = player.choices[letter]
                for element, value in dict_.items():
                    result_dict[letter][element].append(value)
        result_list = []
        for letter, dict_ in result_dict.items():
            for key, value_list in dict_.items():
                result_list.append(self.process_list(letter, value_list))
        winning_indices, sums = self.find_winner(result_list)
        return (winning_indices, sums)


if __name__ == '__main__':
    number_of_players, first_letter = init()
    game = Game(number_of_players, first_letter)
    game.play_game()
    winning_indices, sums = game.score.compute_scores()
    print(f"Indices with highest scores is: {winning_indices}")
    print(f"Sums of each index: {sums}")
