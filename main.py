from random import choice
import hangman, words as hangedman_words

def main(*args, **kwargs):
    words : list[str] = hangedman_words.word_list
    # word should be a random word from words
    word : str  = choice(words)
    # print("_" * len(word)) # to get the playing ground

    guesses : list[str] = []
    lives = 5 # counter to keep track of how many correct guesses
    board = ["_"] * len(word)
    hanged_man_stages = hangman.stages
    gameover = False

    while not gameover:
        # main game loop
        print(hanged_man_stages[lives])
        print(f"{' '.join(board)}")
        guess = input("\nPlease enter a character: ").lower().replace(" ", "")
        
        if guess in guesses:
            print("You've already guessed this dood. . . : ", guess)
            continue

        for index,char in enumerate(word):
            if char == guess:
                guesses.append(guess)
                board[index] = char
                # print where the character goes in the word

        if guess not in word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")

            lives -= 1
            if lives == 0 :
                print("You Died pleb ~!")
                gameover = True
        
        if "_" not in board:
            gameover = True
            print("You've Won~!")
    
    print(word)

if __name__ == "__main__":
    main()