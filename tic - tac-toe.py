import random
Board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
c_p = "X"
game_running = True
def display(Board):
    print(Board[0], '|', Board[1], '|', Board[2])
    print("---------")
    print(Board[3], '|', Board[4], '|', Board[5])
    print("---------")
    print(Board[6], '|', Board[7], '|', Board[8])
def user_input(Board):
    global c_p
    U_I = int(input("Enter the position (0-8): "))
    if 0 <= U_I <= 8 and Board[U_I] == "-":
        Board[U_I] = c_p
    else:
        print("Invalid input")
# def comuter(board):
#    while c_p=="0":
#      posi = random.randint(0,8)
#      if Board[posi]=="_":
#        Board[posi]="0"
def computer_input(Board):
    global c_p
    while True:
        C_I = random.randint(0, 8)
        if Board[C_I] == "-":
            Board[C_I] = c_p
            break
def switch_player():
    global c_p
    if c_p == "X":
        c_p = "O˛"
    else:
        c_p = "X"
def check_winner(Board):
    # Define winning combinations for rows, columns, and diagonals
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)  # diagonals
    ]
    # Check each winning combination
    for combo in winning_combinations:
        if Board[combo[0]] == Board[combo[1]] == Board[combo[2]] != "-":
            return True
    return False
while game_running:
    display(Board)
    if c_p == "X":
        user_input(Board)
    else:
        computer_input(Board)
    if check_winner(Board):
        display(Board)  # Display the final board state
        print(f"Player {c_p} wins!")
        game_running = False
    else:
        switch_player()

