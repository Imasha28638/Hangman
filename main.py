import random

#import modules
import hangmanArts
import wordlist

#if your module has few variables or functions, you can import them directly
# from hangmanArts import title, HANGMANPICS, win, loose

print(hangmanArts.title)

chosen_word = random.choice(wordlist.word_list)
# print(chosen_word)

word_length = len(chosen_word)

placeholder = []
check_letter = []
lives = 6

for _ in range(word_length):
    placeholder.append("_")

print("".join(placeholder))

game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in check_letter:
        print("You already guessed that letter. Try again.\n")
        continue
    else:
        check_letter.append(guess)
    
    for letter in range(word_length):
        if chosen_word[letter] == guess:
            placeholder[letter] = guess
    
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess! You choose {guess}. You lose a life. Lives left: {lives}")
        if lives == 0:
            print(hangmanArts.loose)
            print(hangmanArts.HANGMANPICS[6 - lives])
            print("\nGame Over! The word was:", chosen_word)
            break

    print("\n")
    print(hangmanArts.HANGMANPICS[6 - lives])
    print(" ".join(placeholder))
    print("******************************")

    if "_" not in placeholder:
        print(hangmanArts.win)
        print("\nCongratulations! You've guessed the word:", chosen_word)
        game_over = True
