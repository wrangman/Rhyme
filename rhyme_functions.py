'''
RHYME_FUNCTIONS.PY: Functions to main game

__author__  = "Johan Wrangö"
__version__ = "1.0.0"
__email__   = "johan.wrango@ntig.se"
'''

def splash_screen(which):
    if which == 1:
        print("""
==[ WELCOME TO THE RHYMING GAME ] ===== [v.1.0.0] ==
This is a simple game. Just type a full, valid word
- with one syllable - that rhymes with 'light' (but 
no duplicates, nor names like dwight, brite, wright, 
or leyte).

You have five attempts every turn to choose a valid
rhyme.

- If you run out of attempts you lose,
- If you run out of rhymes you lose,
- If you know more words than me you win! 
- If you give up just hit ENTER.

====================================================""")
    elif which == 2:
        print("""
==[ THE RHYMING GAME ] =============================

- If you run out of attempts you lose,
- If you run out of rhymes you lose,
- If you know more words than me you win! 
- If you give up just hit ENTER.

====================================================""")
        