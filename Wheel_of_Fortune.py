import numpy as np
import time

Category = "Artist & Song"
Phrase = "Cricket is a gentlemen's game"
Phrase = "Hello"

Wheel = ["10", "500", "250", "700", "300", "90", "Bankrupt", "600", "400", "650", "900", "450", "Lose Turn", "100", "550", "800", "750", "150"] # All in dollars

def spin_wheel(wheel):
    out = wheel[np.random.randint(len(wheel))]
    if(not(out == "Bankrupt" or out == "Lose Turn")):
        print("Spinning Wheel.................... $", out)
    else:
        print("Spinning Wheel....................", out)
    return out
def check_string_guessed():
    if('_' not in Phrase):return True
    return False
def next_turn(Turn, PlayersList):
    if(Turn == len(PlayersList)-1):return 0
    else:return(Turn+1)
def find_occurrences(s, ch):
    return [i for i, letter in enumerate(s) if ((ord(letter) == ord(ch)) or (ord(letter) == ord(ch)+32) or (ord(letter) == ord(ch)-32))]
def check_char(char):
    if( len(char) == 1 and ((ord(char)>=65 and ord(char)<=90) or (ord(char)>=97 and ord(char)<=122)) ):return True
    return False
def print_guessed_phrase(Current_Player):
    for i in Current_Player.guessed_phrase:
        print(i, end="")
def check_vowel(ch):
    if(len(ch) == 1 and (ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
    or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u')):
        return True
    return False
def check_guess_complete_for_every_player(PlayersList):
    for i in PlayersList:
        if(i.check_guess_complete() == True):
            return True
    return False

class Player():
    def __init__(self, Name):
        self.name = Name
        self.cash = 0
        self.prizes = []
        self.guessed_phrase = []
        for i in Phrase:
            if(check_char(i)):self.guessed_phrase.append("_")
            else:self.guessed_phrase.append(i)

    def add_cash(self,amount):
        self.cash += amount
        self.prizes.append("$"+str(amount))

    def bankrupt(self):
        self.cash = 0
        self.prizes = []

    def check_guess_complete(self):
        if("_" not in self.guessed_phrase):
            print('\n\n', self.name, " guessed it correctly\n\n", sep = "")
            return True
        return False

    def print_possessions(self):
        print("Player : "+ self.name+ "\nBalance : $"+ str(self.cash)+ "\nPrizes Earned : "+ str(self.prizes), '\n')

    def __str__(self):
        return(self.name)
#------------------------------------------------------------------------------

blanks = ""
Turn = -1
for i in Phrase:
    if(check_char(i)):blanks+=("_")
    else:blanks+=i

print("\n================================ W H E E E L   O F   F O R T U N E ========================\n                  \
(Note : Vowels cost $250, all other letters are free to guess)\n\n\nCategory :",Category, "\nPhrase : ", blanks, end = "")
print('\n\n')

PlayersList = []
NoOfPlayers = int(input("Enter number of players playing this game(must be 2 or more) : "))
while(NoOfPlayers<=1):
    NoOfPlayers = int(input("Number of players must be 2 or more. Enter again : "))

for i in range(NoOfPlayers):
    inp = input("Player "+ str(i+1)+ " Name : ")
    inp = Player(inp)
    PlayersList.append(inp)
print('\n\n')

while(not check_guess_complete_for_every_player(PlayersList)):

    Turn = next_turn(Turn, PlayersList)
    print(PlayersList[Turn], "'s Turn ", sep = "")

    Prize = spin_wheel(Wheel)


    if(Prize == "Bankrupt"):#------------------------------------Bankrupt
        PlayersList[Turn].bankrupt()
        PlayersList[Turn].print_possessions()


    elif(Prize == "Lose Turn"):#------------------------------------Player Lost its turn
        print(PlayersList[Turn], "lost its turn\n\n")


    else:#-----------------------------------------------------------Player won cash
        Choice = input(" 1.Guess a Letter\n 2.Guess Complete Phrase\n 3.Pass your Turn to next Player\nYour Choice(1, 2, or 3) : ")
        while(not(Choice == "1" or Choice == "2" or Choice == "3")):
            Choice = input("Wrong Choice. Please choose 1, 2, or 3 : ")

        if(Choice == "1"):
            input_letter = input("Enter character(except space) : ")
            while(not check_char(input_letter)):
                print("Not a valid character. Try again")
                input_letter = input("Enter character(exept space) : ")

            if(check_vowel(input_letter)):
                if(PlayersList[Turn].cash >= 250):
                    pass
                else:
                    if(input_letter != "pass"):
                        while(check_vowel(input_letter)):
                            print("Vowels cost $250, but you only have $", PlayersList[Turn].cash,
                            ". You can either guess a non-vowel letter or pass your turn to next player by entering \"pass\"")
                            input_letter = input("Enter character(exept space) : ")
                            if(input_letter != "pass"):
                                while(not check_char(input_letter)):
                                    print("Not a valid character. Try again")
                                    input_letter = input("Enter character(exept space) : ")

            if(input_letter == "pass"):
                print("Turn passed on to next player\n\n")
            else:
                occurances_array = find_occurrences(Phrase, input_letter)
                PlayersList[Turn].add_cash(int(Prize)*len(occurances_array))
                if(len(occurances_array) == 0):
                    print("Wrong guess.", input_letter, "character is not in the Phrase")
                else:
                    for p in occurances_array:
                        PlayersList[Turn].guessed_phrase[p] = Phrase[p]
                print_guessed_phrase(PlayersList[Turn])
                print('\n\n')


        elif(Choice == "2"):
            input_phrase = input("Enter the complete phrase(with spaces and proper Capitalization) :")
            if(input_phrase == Phrase or input_phrase == Phrase):
                print("Congratulations! You guessed it right\n", PlayersList[Turn], " wins\n\n", sep = "")
            else:
                print("Not the correct guess\n\n")


        elif(Choice == "3"):
            print("Turn passed on to next player\n\n")


for i in PlayersList:
    i.print_possessions()