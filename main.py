from helpers import clear_output, display_board, player_input, place_marker, win_check, choose_first, space_check, full_board_check, player_choice, replay  

# triggers top loop to start the game
game_on = True

print('Welcome to Tic Tac Toe!')

while game_on:

  # set up game variables
  choices = player_input()
  current_player = choose_first()
  board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
  winner = None

  print(f'Player {current_player} will go first!')

  # starts the round - round continues until there is a winner
  while winner == None: 

    # first check to see if the board is full
    if full_board_check(board):
      winner = 0
      break
    # otherwise, start the turn
    else:
      print(f'Player {current_player}, your turn!')

      # display the board and prompt user to select their next position
      display_board(board)
      next_position = player_choice(board)
      place_marker(board, choices[current_player], next_position)
      
      # check for a winner
      check = win_check(board, choices[current_player])

      clear_output()

      # if there is a winner, set the winner to the current player. if not, set the current player to the next player.
      if check:
        winner = current_player
        break
      else:
        if current_player == 1:
          current_player = 2
        elif current_player == 2:
          current_player = 1
  
  # determine what message to output at the end of a game
  if winner != 0:
    print(f'Congratulations, Player {current_player}, you won!')
  else:
    print('Board is full, nobody wins!')

  # prompt user for replay
  game_on = replay()
  continue