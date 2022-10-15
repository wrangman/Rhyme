import random
import os    
import time
from msvcrt import getwch
from colors import bcolors
from rhyme_functions import splash_screen


def check_rhyme(what_rhyme, what_word):
    if what_rhyme == "light":
        if what_word in rhymes_used:
            return False    #word already used - no go!
        else:
            return True     #Word not used - go ahead        
    

def check_validity(what_rhyme, what_word):
    if what_rhyme == "light":
        if what_word in rhymes_light:
            return True    #word rhymes!
        else:
            return False     #Word does not rhyme
        
    
def ai_feedback():
    quick_feedback = ["Good!",
                      "Nice.",
                      "Good.",
                      "You got lucky ;)",
                      "Nicely done!",
                      "Sweet!",
                      "OK!",
                      "Nice choice.",
                      "Hmm...",
                      "Excellent!",
                      "Awesome!",
                      "Fine job.",
                      "Aha! That one.",
                      "OK.",
                      "Very nice.",
                      "Superb!"]

    x = random.randint(0, len(quick_feedback) - 1)

    return quick_feedback[x]


def ai_comment():
    quick_comment = ["I choose",
                     "I pick",
                     "I'll go with",
                     "My turn",
                     "My choice",
                     "Let's try",
                     "Rhymes with",
                     "My word"]
 
    x = random.randint(0, len(quick_comment) - 1)

    return quick_comment[x]


def check_rhyme(what_rhyme, what_word):
    if what_rhyme == "light":
        if what_word in rhymes_used:
            return False    #word already used - no go!
        else:
            return True     #Word not used - go ahead        
    

def check_validity(what_rhyme, what_word):
    if what_rhyme == "light":
        if what_word in rhymes_light:
            return True       #word rhymes!
        else:
            return False     #Word does not rhyme
        

rhymes_light = ["knight",
                "bright",
                "fright",
                "flight",
                "fight",
                "night",
                "shite",
                "blight",
                "right",
                "tight",
                "sight",
                "white",
                "plight",
                "slight",
                "might",
                "height",
                "nite",
                "aiit",
                "bite",
                "pike",
                "kite",
                "rite",
                "lite",
                "cite",
                "spite",
                "trite",
                "quite",
                "dight",
                "bight",
                "byte",
                "mite",
                "site",
                "sleight",
                "smite",
                "sprite",
                "twite",
                "wight",
                "write"]

first_game = 1

while True:
    os.system('cls')
    rhymes_used = []

    total_light_words = len(rhymes_light)
    total_words_played = 0
    turns_left = 5
    current_rhyme = "light"
    still_playing = True

    print(bcolors.YELLOW)
    splash_screen(first_game)
    print(bcolors.CYAN + f"\nLet's play words that rhyme with {current_rhyme}.\nYou start. Good luck!\n")

    while True:
        if total_words_played == total_light_words:             #No more rhymes - player loses!           
            game_state = 1
            still_playing = False
            break

        total_words_played += 1
        
        while True:
            if turns_left == 0:                                 #No more attempts - player loses!
                game_state = 4
                still_playing = False
                break
            
            print(bcolors.YELLOW + f"{total_words_played}) " + bcolors.ENDC + "Your turn: ", end="")
            entry = input(bcolors.YELLOW).lower()
            entry = entry.replace(" ", "")
            
            if entry == "":
                game_state = 3
                still_playing = False        
                break
            
            if still_playing:
                if not check_validity(current_rhyme, entry):
                    turns_left -= 1
                    print(bcolors.FAIL + f"Sorry, that doesn't rhyme! You have: {turns_left} attempt(s) left.\n")
                    continue
                
                if check_rhyme(current_rhyme, entry):
                    turns_left = 5
                    rhymes_used.append(entry)
                    break
                else:
                    print(bcolors.CYAN + "The word has already been played. Try again!\n")
                    continue
        
        if not still_playing: break
    
        if total_words_played == total_light_words:
            game_state = 2
            still_playing = False
            break
        
        while True:
            what_word = random.randint(0, total_light_words - 1)
            ai_choice = rhymes_light[what_word]
            
            if ai_choice in rhymes_used:
                continue
            else:
                total_words_played += 1
                rhymes_used.append(ai_choice)
                break
        
        give_feedback = ai_feedback()
        give_comment = ai_comment()
    
        print(bcolors.YELLOW + f"{total_words_played}) " + bcolors.ENDC + f"{give_feedback} {give_comment}: " + bcolors.YELLOW + f"{ai_choice}\n")

    if game_state == 1:
        print(bcolors.GREEN + bcolors.BOLD + "YOU WIN - I don't know any more words!")
    elif game_state == 2:
        print(bcolors.FAIL + bcolors.BOLD + "I WIN - There are no more rhymes!")
    elif game_state == 3:
        print(bcolors.FAIL + bcolors.BOLD + "I WIN - You gave up!")
    elif game_state == 4:
        print(bcolors.FAIL + bcolors.BOLD + "I WIN - You ran out of attempts!")
        

    print(bcolors.YELLOW + "\nPlay again? (Y)es / (N)o ", end="")
    key_stroke = getwch().upper() 
        
    if key_stroke == "N":    
        print(bcolors.CYAN + "\nThanks for playing!")
        print(bcolors.ENDC)                 # Restore default system colors
        time.sleep(2)
        exit()
    else:
        first_game = 2
        continue