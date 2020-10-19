# Wheel-of-Fortune
It is a game called "Wheel of Fortune" implemented in python3 through Object Oriented Programming.

There are num_human human players and num_computer computer players.
Every player has some amount of money ($0) at the start of the game
Every player has a set of prizes (none at the start of the game)
The goal is to guess a phrase within a category. For example:
Category: Artist & Song
Phrase: Cricket is a gentlemen's game
Players see the category and an obscured version of the phrase where every alphanumeric character in the phrase starts out as hidden (using underscores: _):

Category: Artist & Song
Phrase: _______ __ _ _________'_ ____

During their turn, every player spins the wheel to determine a prize amount and:

If the wheel lands on a cash square, players may do one of three actions:

  Guess any letter that hasn’t been guessed by typing a letter (a-z)

    Vowels (a, e, i, o, u) cost () to guess and can’t be guessed if the player doesn’t have enough money. All other letters are “free” to guess

    The player can guess any letter that hasn’t been guessed and gets that cash amount for every time that letter appears in the phrase

    If there is a prize, the user also gets that prize (in addition to any prizes they already had)

    If the letter does appear in the phrase, the user loses its turn.

    Example: The user lands on () and guesses ‘W’

    There are three W’s in the phrase, so the player wins ()

  Guess the complete phrase by typing a phrase (anything over one character that isn’t ‘pass’)

    If they are correct, they win the game
    If they are incorrect, it is the next player’s turn

  Pass their turn by entering 'pass'

If the wheel lands on “lose a turn”, the player loses their turn and the game moves on to the next player

If the wheel lands on “bankrupt”, the player loses their turn and loses their money but they keep all of the prizes they have won so far.

The game continues until the entire phrase is revealed (or one player guesses the complete phrase)
