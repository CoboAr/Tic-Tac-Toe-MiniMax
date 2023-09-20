# Tic-Tac-Toe-MiniMax

## Demo
https://github.com/CoboAr/Tic-Tac-Toe-MiniMax/assets/144629565/bbde3b9e-8572-47e9-a691-87b9ccaff16c

## What is Minimax?
A minimax algorithm is a recursive program written to find the best gameplay that minimizes any tendency to lose a game while maximizing any opportunity to win the game.

## How does it work?
In most cases, the player that initially invokes minimax is called the maximizing player. In other words, the original invocator of minimax is the player that wants to maximize any opportunity to win the game. In contrast, the maximizing player’s opponent is called the minimizing player. As such, the minimizing player is the player whose chances of winning must be minimized. Minimax algorithm searches recursively for the optimal move that leads to the Max player winning or drawing. It considers the current state of the game and the possible moves at that point, then plays (alternating min and max) for each legitimate move until it reaches a terminal state (win, draw, or loss).

## Adapted pseudocode of the Algorithm

```
minimax (state, player)
  max_player = letter of AIPlayer
  other_player = "X" if AIPlayer =="O" else "O"

  if (current_winner = other_player)
    return (position,score)
  else if there are no more empty positions
    return (position:None, score:0)
  if player = max_player
      best_score = -INFINITY
  else
      best_score = +INFINITY

  for possible_moves in available_moves
      make_move(possible_move,player)
      simulated_score = minimax(state, other_player)

  undo move

  simulated_score[position] = possible move

  if player = max_player
      if simulated_score > best_score
        best_score = simulated_score #max value
  else
      if simulated_score < best_score
      best_score = simulated_score  #min value

  return best_score
```
## Author
## Arnold Cobo
