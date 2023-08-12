# Initialize an empty 5x5 game board with "O" representing ocean
board = []

for i in range(5):
    board.append(["O"] * 5)

# Function to print the game board
def print_board(board):
    for row in board:
        print(" ".join(row))

# Print the initial game board
print_board(board)

# Generate random coordinates for hiding the battleship
from random import randint

# Function to get a random row coordinate
def random_row(board):
    return randint(0, len(board) - 1)

# Function to get a random column coordinate
def random_col(board):
    return randint(0, len(board) - 1)

# Get random coordinates for the battleship
ship_row = random_row(board)
ship_col = random_col(board)

# Loop for a maximum of 4 turns
for turn in range(4):
    print("Turn", turn + 1)

    # Get the player's guesses for row and column
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    # Print the actual battleship location (for debugging purposes)
    print(ship_row)
    print(ship_col)

    # Check if the player's guess matches the battleship's location
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        break
    else:
        # Check if the guess is out of bounds or if the player already guessed there
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops, that's not in the ocean")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already")
        else:
            # Display "miss" message, update the board, and print the updated board
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
            print_board(board)
            
            # Check if it's the last turn and end the game if needed
            if turn == 3:
                print("Game over")
                
        # Print the current state of the board
        print_board(board)
