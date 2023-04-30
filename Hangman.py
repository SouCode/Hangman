import random


class Word:
    def __init__(self, chosen_word):
        self.chosen_word = chosen_word
        # I create a list of dictionaries to represent the word's status
        self.word_status = [{"letter": letter, "guessed": False} for letter in chosen_word]

    def update_status(self, guessed_letter):
        correct_guess = False
        # I loop through the word_status to update the guessed letters
        for letter in self.word_status:
            if letter["letter"] == guessed_letter:
                letter["guessed"] = True
                correct_guess = True
        return correct_guess

    def word_guessed(self):
        # I check if all letters have been guessed
        for letter in self.word_status:
            if not letter["guessed"]:
                return False
        return True

    def display_word(self):
        display = ""
        # I create the display of the word with guessed letters and underscores
        for letter in self.word_status:
            if letter["guessed"]:
                display += letter["letter"] + " "
            else:
                display += "_ "
        return display.strip()


def main():
    # I set up the word list and choose a random word
    word_list = ["apple", "banana", "cherry", "grape", "kiwi", "mango", "orange", "papaya", "strawberry"]
    chosen_word = random.choice(word_list)
    word = Word(chosen_word)

    # I initialize remaining_guesses and letters_used
    remaining_guesses = 8
    letters_used = []

    # I start the game loop
    while remaining_guesses > 0:
        print(word.display_word())
        guess = input("Please guess a letter: ").lower()

        # I check if the input is a single letter
        if not guess.isalpha() or len(guess) != 1:
            print("That is not a letter.")
            continue

        if guess in letters_used:
            print("You've already guessed this letter.")
            continue

        # I add the guessed letter to the list of used letters
        letters_used.append(guess)
        correct_guess = word.update_status(guess)

        # I check if the guess is correct and update the game state accordingly
        if correct_guess:
            print("Yes!")
            if word.word_guessed():
                print("Congratulations, you've guessed the word:", chosen_word)
                break
        else:
            remaining_guesses -= 1
            print("No, silly.")
            if remaining_guesses == 0:
                print("Game over—Lose! The word was:", chosen_word)
                break

        # I display remaining guesses and used letters
        print("Remaining guesses:", remaining_guesses)
        print("Letters used:", ", ".join(letters_used))
        print()


if __name__ == "__main__":
    main()
