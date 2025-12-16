from random import randint

def main():
    hangman("test.txt")
    
def hangman(filename):
    guess = ""
    rand_word = random_word(filename)
    hm_string = '_' * len(rand_word)
    guessed = []
    num_guesses = 0
    
    while(guess != rand_word):
        if (hm_string == rand_word):
            print("Hurray you guessed the word: ", rand_word)
            break
        
        if num_guesses > 7:
            print("You used up all your guesses.")
            print("GAME OVER!")
            break
        print(hm_string)
        guess = input("\nGuess a letter\n" )
        
        if guess in guessed:
            print("You have already guessed: ", guess)
            continue
        
        guessed.append(guess)
        
        if (guess in rand_word):
            for i in range(0, len(rand_word)):
                if rand_word[i] == guess:
                    hm_list = list(hm_string)
                    hm_list[i] = guess
                    hm_string = "".join(hm_list)
        else:
            num_guesses += 1
        
        hangman_drawing(num_guesses)

def hangman_drawing(num_guesses):
    if num_guesses == 1:
        print("#####")
    elif num_guesses == 2:
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("#####")
    elif num_guesses == 3:
        print("   ___")
        print("  |   |")
        print("  |   ")
        print("  |")
        print("  |")
        print("#####")
    elif num_guesses == 4:
        print("   ___")
        print("  |   |")
        print("  |   O")
        print("  |")
        print("  |")
        print("#####")
    elif num_guesses == 5:
        print("   ___")
        print("  |   |")
        print("  |   O")
        print("  |  ´|`")
        print("  |")
        print("#####")
    elif num_guesses == 6:
        print("   ___")
        print("  |   |")
        print("  |   O")
        print("  |  ´|`")
        print("  |   '\\")
        print("#####")
    elif num_guesses == 7:
        print("   ___")
        print("  |   |")
        print("  |   O")
        print("  |  ´|`")
        print("  |  /'\\")
        print("#####")
            
            

def random_word(filename):
    with open(filename) as file:
        string_file = file.read()
        word_list = string_file.split("\n")
        rand_index = randint(0, len(word_list) - 1)
        rand_word = word_list[rand_index]
        
    return rand_word
        
if __name__ == "__main__":
    main()