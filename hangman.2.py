#Hangman, the game
#Jones, Ashton
import random
import os

path = "data"

def start_screen():
    print("")
    file = "art/start.txt"
    with open(file, "r") as f:
        lines = f.read()
    print(lines[2:])
    print("")

def end_screen():
    print("")
    file = "art/end.txt"
    with open(file, "r") as f:
        lines = f.read()
    print(lines[9:])
    print("")

def get_puzzle():
    path = "data"
    puzz_file = ""
    file_names = os.listdir(path)
    
    for i, f in enumerate(file_names):
        open(f, 'r')
        category_name = lines[0]
        print(str(i + 1) + ") " + f)

    choice = input("Pick One Fam  ")
    choice = int(choice) - 1

    file = path + "/" + file_names[choice]

    with open(file, "r") as f:
        lines = f.read().splitlines()
        
    puzzle = random.choice(lines[1:])
        
    return random.choice( lines[1:] )

def get_solved(puzzle, guesses):
    solved = ""
    for letter in puzzle:
        if letter.lower() in guesses.lower():
            solved += letter
        else:
            solved += "-"
    return (solved)


def check_strikes(puzzle, guesses, strikes):
        if guesses[-1] in puzzle:
            return strikes
        strikes += 1
        return strikes
            
def get_guess():
    print()
    letter = input("Enter a Letter to guess the word.")
    print()
    if len(letter) <= 1:
        return str(letter)
    else:
        print("You can only type in one letter at a time you fool!")
        return get_guess()
            
def display_board(solved, guesses, strikes):
    print(solved)
    print("")
    f = open('art/strikes.txt', 'r')
    if strikes == 1:
        one = f.readline()
        print(one)
    elif strikes == 2:
        two = f.readline()
        print(two)
    elif strikes == 3:
        three = f.readline()
        print(three)
    elif strikes == 4:
        four = f.readline()
        print(four)
    elif strikes == 5:
        five = f.readline()
        print(five)
    elif strikes == 6:
        six = f.readline()
        print(six)


def show_result(strikes, limit, puzzle):
    if strikes == limit:
        print("""           GCSD
       URL Blocked
URL:www.coolmath-game.com

     category: games


You lost, R.I.P coolmath. The word was """ + puzzle)
    else:
        print()
        print("You got it in " + str(limit - strikes) + " guesses.")
        

def play():
    strikes = 0
    limit = 7
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)
    display_board(solved, guesses, strikes)

    while solved != puzzle and strikes != limit:
        if strikes != limit:
            print("You have " + str(limit - strikes) + " guesses left until GCSD blocks www.coolmath-games.com")
            print()
            guesses += get_guess()
            solved = get_solved(puzzle, guesses)
            strikes = check_strikes(puzzle, guesses, strikes)
            display_board(solved, guesses, strikes)
        else:
            print("You ran out of guesses fam wow.")
            print()

    show_result(strikes, limit, puzzle)

def play_again():
    print()
    while True:
        decision = input("Would you like to play again? (y/n) ")
        decision = decision.upper()
        print()
        if decision == 'Y' or decision == 'YES':
            return True
        elif decision == 'N' or decision == 'NO':
            return False
        else:
            print()
            print("Answer it right you mongrel. Would you like to play again? (y/n)")


start_screen()

playing = True
while playing == True:
    play()
    playing = play_again()

end_screen()
