import random

def hangman():
    words = ['python', 'java', 'kotlin', 'javascript', 'hangman']
    word = random.choice(words)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print(f"You have {max_incorrect} incorrect guesses allowed.\n")

    while True:
        # Display the current progress
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print("Word: ", display_word)

        if '_' not in display_word:
            print("Congratulations! You guessed the word correctly!")
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.\n")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print("Good guess!\n")
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess! You have {max_incorrect - incorrect_guesses} guesses left.\n")
            guessed_letters.add(guess)

            if incorrect_guesses >= max_incorrect:
                print(f"Game Over! The word was '{word}'. Better luck next time!")
                break

if __name__ == "__main__":
    hangman()
