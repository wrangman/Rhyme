'''
RHYME.PY: The Rhyming Game!

__author__  = "Johan Wrangö"
__version__ = "1.0.2"
__email__   = "johan.wrango@ntig.se"
'''

import random
import os    
import time
from msvcrt import getwch
from colors import bcolors
from rhyme_functions import splash_screen


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
                      "Ah! That one.",
                      "Alright.",
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
                     "What about",
                     "Here's one",
                     "Did you know",
                     "An easy one",
                     "Rhymes with",
                     "My rhyme",
                     "My word"]
 
    x = random.randint(0, len(quick_comment) - 1)

    return quick_comment[x]


def check_rhyme(what_word):
    if what_word in rhymes_used:
        return False    #Word already used - no go!
    else:
        return True     #Word not used - go ahead        


def check_validity(what_word):
    if what_word in rhymes_light:
        return True      #Word rhymes!
    else:
        return False     #Word does not rhyme
    

def play_word(word):
    index = rhymes_light.index(word)     #Find pos of rhyme
    rhymes_light.pop(index)              #Remove rhyme from rhyme list
    rhymes_used.append(word)


def get_rhymes():
    rhymes = ["knight",
              "wright",
              "bright",
              "fright",
              "flight",
              "fight",
              "night",
              "shite",
              "blight",
              "right",
              "blite",
              "tight",
              "sight",
              "white",
              "plight",
              "slight",
              "flite",
              "might",
              "height",
              "leyte",
              "nite",
              "aiit",
              "bite",
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
    return rhymes


def get_hint():
    ai_hint = get_word()
    print(bcolors.CYAN + f"Here's a hint for next time: '{ai_hint}.'")


def get_word():
    what_word = random.randint(0, len(rhymes_light) - 1)
    ai_choice = rhymes_light[what_word]    
    return ai_choice


first_game = 1

while True:
    os.system('cls')

    rhymes_used = []
    rhymes_light = get_rhymes()
    total_words_played = 0
    turns_left = 5
    still_playing = True

    print(bcolors.YELLOW)
    splash_screen(first_game)
    print(bcolors.CYAN + f"\nLet's play words that rhyme with 'light.'\nYou start. Good luck!\n")

    while True:
        if not rhymes_light:                                    #No more rhymes - draw!     
            game_state = 2
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
            
            if entry == "idkfa":                                #Player cheats 
                print(bcolors.CYAN + "Cheating mode activated.")

                entry = get_word()   
                if len(rhymes_light) > 1: print(rhymes_light)
                print(bcolors.YELLOW + f"{total_words_played}) " +  bcolors.ENDC + "Your turn: " + bcolors.YELLOW + entry)
            
            if entry == "":                                     #Player exits / gives up
                game_state = 3
                still_playing = False        
                break
        
            if check_rhyme(entry):                              #Has the rhyme been played already?
                if not check_validity(entry):                   #Is it a valid word?
                    turns_left -= 1
                    print(bcolors.FAIL + f"Sorry, that doesn't rhyme! You have: {turns_left} attempt(s) left.\n")
                    continue
                else:                                           #Valid choice
                    turns_left = 5
                    play_word(entry)
                    break
            else:                                               #Word has already been played
                turns_left -= 1
                print(bcolors.FAIL + F"The word has already been played. You have: {turns_left} attempt(s) left.\n")
                continue
    
        if not still_playing: break                             #Player quit or lost

        if len(rhymes_light) <= 0:                                    #No more rhymes - player wins / knows more words!
            game_state = 1
            still_playing = False
            break

        total_words_played += 1 
        ai_choice = get_word()
        play_word(ai_choice)
        
        give_feedback = ai_feedback()
        give_comment = ai_comment()
    
        print(bcolors.YELLOW + f"{total_words_played}) " + bcolors.ENDC + f"{give_feedback} {give_comment}: " + bcolors.YELLOW + f"{ai_choice}\n")

    if game_state == 1:
        print(bcolors.GREEN + bcolors.BOLD + "YOU WIN - I don't know any more rhymes!")
    elif game_state == 2:
        print(bcolors.CYAN + bcolors.BOLD + "IT'S A TIE - There are no more rhymes!")
    elif game_state == 3:
        print(bcolors.FAIL + bcolors.BOLD + "I WIN - You gave up!")
        get_hint()
    elif game_state == 4:
        print(bcolors.FAIL + bcolors.BOLD + "I WIN - You ran out of attempts!")
        get_hint()
        
    print(bcolors.YELLOW + "\nPlay again? (Y)es / (N)o ", end="")
    key_stroke = getwch().upper() 
        
    if key_stroke == "N":    
        print(bcolors.CYAN + "\nSee you next time!")
        print(bcolors.ENDC)                 # Restore default system colors
        time.sleep(2)
        exit()
    else:
        first_game = 2                      # Wanna play again - show different splash screen
        continue