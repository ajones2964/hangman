tries = 0
def get_puzzle():
    puzzle = "minceraft"
    return puzzle.lower()

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess():
    letter = input("Guess a letter: ")
    return letter.lower()

def display_board(solved):
    print(solved)

def graphic(tries):
    if tries == 0:
        print("""
GCSD                Games
_________________________
Guess the word right to save
your Games from evil GCSD""")
    if tries == 1:
        print("""   GCSD             Games
_________________________""")
    elif tries == 2:
        print("""     GCSD           Games
_________________________""")
    elif tries == 3:
        print("""         GCSD       Games
_________________________""")
    elif tries == 4:
        print("""             GCSD   Games
_________________________""")
    elif tries == 5:
        print("""                GCSDGames
_________________________""")
    elif tries == 6:
        print("""              URL Blocked
_________________________""")

def show_result():
    print("You Win")
    
def play():
    puzzle = get_puzzle()
    guesses = ""
    tries = 0
    solved = get_solved(puzzle, guesses)

    limit = 6

    while solved != puzzle or tries != limit:
        display_board(solved)
        graphic(tries)
        letter = get_guess()

        if letter not in puzzle:
            tries += 1
        guesses += letter
        solved = get_solved(puzzle, guesses)
        

    show_result()
    
play()
