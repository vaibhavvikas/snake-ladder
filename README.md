## Snake Ladder Game

A python snake and ladder game for machine coding.


* Free software: MIT license
* Documentation: https://snake-ladder.readthedocs.io.


## Problem Statement
Create a snake and ladder application. The application should take as input (from the command line or a file):

1. Number of snakes (s) followed by s lines each containing 2 numbers denoting the head and tail positions of the snake.
2. Number of ladders (l) followed by l lines each containing 2 numbers denoting the start and end positions of the ladder.
3. Number of players (p) followed by p lines each containing a name.

After taking these inputs, you should print all the moves in the form of the current player name followed by a random number between 1 to 6 denoting the die roll and the initial and final position based on the move.
Format: <player_name> rolled a <dice_value> and moved from <initial_position> to <final_position>

When someone wins the game, print that the player won the game.
Format: <player_name> wins the game

## Rules of the game

1. The board will have 100 cells numbered from 1 to 100.
2. The game will have a six sided dice numbered from 1 to 6 and will always give a random number on rolling it.
3. Each player has a piece which is initially kept outside the board (i.e., at position 0).
4. Each player rolls the dice when their turn comes.
5. Based on the dice value, the player moves their piece forward that number of cells. Ex: If the dice value is 5 and the piece is at position 21, the player will put their piece at position 26 now (21+5).
6. A player wins if it exactly reaches the position 100 and the game ends there.
7. After the dice roll, if a piece is supposed to move outside position 100, it does not move.
8. The board also contains some snakes and ladders.
9. Each snake will have its head at some number and its tail at a smaller number.
10. Whenever a piece ends up at a position with the head of the snake, the piece should go down to the position of the tail of that snake.
11. Each ladder will have its start position at some number and end position at a larger number.
12. Whenever a piece ends up at a position with the start of the ladder, the piece should go up to the position of the end of that ladder.
13. There could be another snake/ladder at the tail of the snake or the end position of the ladder and the piece should go up/down accordingly.
14. Assumptions you can take apart from those already mentioned in rules
15. There won’t be a snake at 100.
16. There won’t be multiple snakes/ladders at the same start/head point.
17. It is possible to reach 100, i.e., it is possible to win the game.
18. Snakes and Ladders do not form an infinite loop.

## Expectations
1. Make sure that you have a working and demonstrable code
2. Make sure that the code is functionally correct
3. Code should be modular and readable
4. Separation of concern should be addressed
5. Please do not write everything in a single file
6. Code should easily accommodate new requirements and minimal changes
7. There should be a main method from where the code could be easily testable
8. [Optional] Write unit tests, if possible
9. No need to create a GUI

## Optional Requirements
Please do these only if you’ve time left. You can write your code such that these could be accommodated without changing your code much.

1. The game is played with a dice with the dice value could be between 1 to any input in a single move.
2. The board size can be customizable and can be taken as input before other input (snakes, ladders, players).
3. In case of more than 2 players, the game continues until only one player is left.
4. On getting max value, you get another turn and on getting 3 consecutive max values, all the three of those get cancelled.

## Sample Input and Output
```
100
2
vaibh dwan
12
4
87 23
43 11
98 56
76 36
4
12 45
40 60
73 91
62 81
```
```
vaibh rolled a 6 and moved from 0 to 6
dwan rolled a 10 and moved from 0 to 10
vaibh rolled a 10 and moved from 6 to 16
dwan rolled a 27 and moved from 10 to 37
vaibh rolled a 4 and moved from 16 to 20
dwan rolled a 2 and moved from 37 to 39
vaibh rolled a 1 and moved from 20 to 21
dwan rolled a 2 and moved from 39 to 41
vaibh rolled a 11 and moved from 21 to 32
dwan rolled a 4 and moved from 41 to 45
vaibh rolled a 5 and moved from 32 to 37
dwan rolled a 6 and moved from 45 to 51
vaibh rolled a 2 and moved from 37 to 39
dwan rolled a 7 and moved from 51 to 58
vaibh rolled a 1 and moved from 39 to 40
dwan rolled a 6 and moved from 58 to 64
vaibh rolled a 2 and moved from 40 to 42
dwan rolled a 4 and moved from 64 to 68
vaibh rolled a 2 and moved from 42 to 44
dwan rolled a 6 and moved from 68 to 74
vaibh rolled a 11 and moved from 44 to 55
dwan rolled a 6 and moved from 74 to 80
vaibh rolled a 3 and moved from 55 to 58
dwan rolled a 1 and moved from 80 to 81
vaibh rolled a 9 and moved from 58 to 67
dwan rolled a 2 and moved from 81 to 83
vaibh rolled a 3 and moved from 67 to 70
dwan rolled a 5 and moved from 83 to 88
vaibh rolled a 6 and moved from 70 to 76
dwan rolled a 4 and moved from 88 to 92
vaibh rolled a 2 and moved from 76 to 78
dwan rolled a 2 and moved from 92 to 94
vaibh rolled a 10 and moved from 78 to 88
dwan rolled a 9 and but can't move from 94
vaibh rolled a 11 and moved from 88 to 99
dwan rolled a 3 and moved from 94 to 97
vaibh rolled a 5 and but can't move from 99
dwan rolled a 1 and moved from 97 to 98
vaibh rolled a 4 and but can't move from 99
dwan rolled a 1 and moved from 98 to 99
vaibh rolled a 15 and but can't move from 99
dwan rolled a 7 and but can't move from 99
vaibh rolled a 3 and but can't move from 99
dwan rolled a 2 and but can't move from 99
vaibh rolled a 10 and but can't move from 99
dwan rolled a 11 and but can't move from 99
vaibh rolled a 5 and but can't move from 99
dwan rolled a 6 and but can't move from 99
vaibh rolled a 2 and but can't move from 99
dwan rolled a 11 and but can't move from 99
vaibh rolled a 10 and but can't move from 99
dwan rolled a 10 and but can't move from 99
vaibh rolled a 11 and but can't move from 99
dwan rolled a 8 and but can't move from 99
vaibh rolled a 5 and but can't move from 99
dwan rolled a 11 and but can't move from 99
vaibh rolled a 19 and but can't move from 99
dwan rolled a 10 and but can't move from 99
vaibh rolled a 15 and but can't move from 99
dwan rolled a 4 and but can't move from 99
vaibh rolled a 6 and but can't move from 99
dwan rolled a 1 and moved from 99 to 100
Game Over
```

## Credits

This package was created with Cookiecutter_ and the `vaibhavvikas/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`vaibhavvikas/cookiecutter-pypackage`: https://github.com/vaibhavvikas/cookiecutter-pypackage
