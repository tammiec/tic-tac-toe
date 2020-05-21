import random

def clear_output():
  print('\n' * 100)

# Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation. The first item in the list is a throwaway.
def display_board(board):
  print(board[1] + '|' + board[2] + '|' + board[3])
  print('-----')
  print(board[4] + '|' + board[5] + '|' + board[6])
  print('-----')
  print(board[7] + '|' + board[8] + '|' + board[9])


# Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.
def player_input():
  marker = ''
  while not (marker == 'X' or marker == 'O'):
    marker = input('Player 1 - please choose a marker (X or O): ').upper()
  
  if marker == 'X':
    return ('X', 'O')
  else:
    return ('O', 'X')

# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
def place_marker(board, marker, position):
  board[position] = marker
  return board

# Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
def win_check(board, mark):
  return ((board[1] == mark and board[2] == mark and board[3] == mark) or # across top
  (board[4] == mark and board[5] == mark and board[6] == mark) or # across middle
  (board[7] == mark and board[8] == mark and board[9] == mark) or # across bottom
  (board[1] == mark and board[4] == mark and board[7] == mark) or # down left
  (board[2] == mark and board[5] == mark and board[8] == mark) or # down middle
  (board[3] == mark and board[6] == mark and board[9] == mark) or # down right
  (board[1] == mark and board[5] == mark and board[9] == mark) or # diagonal
  (board[3] == mark and board[5] == mark and board[7] == mark)) # diagonal

# Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.
def choose_first():
  return f'Player {random.randint(1,2)}'

# Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.
def space_check(board, position):
  return board[position] == ' '

# Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
def full_board_check(board):
  for i in range(1,10):
    if (space_check(board, i)):
      return False
  return True

# Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.
def player_choice(board):
  next = 0
  while next not in range(1,9) or not space_check(board, next):
    next = int(input('Please select your next position (1-9): '))
  
  return next


# Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
def replay():
  return input('Do you want to play again? (Yes or No): ').lower() == 'yes'