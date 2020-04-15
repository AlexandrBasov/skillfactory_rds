# Guess The Number
Guess the Number is a fun educational game.

## Condition 
The computer makes an integer from 1 to 100, and we need to guess it.
By “to guess” of course, is meant “writing a program that guesses a number.”

## Description of the code
The [guessnumber.py](guessnumber.py) file contains two functions:
```python
def game_core_binary(number):
    ...
```
 and
```python
def score_game (game_core):
    ...
```
The game_core_binary(number) function is a core of our game, it takes a number as input parameter, guesses that number and returns a number of attempts for which the number was guessed.
The score_game (game_core) function is a game process or a game cycle.
As an input parameter, this function takes another function "game_core" that guesses the number and runs that "game_core" function 1000 times.
As a result, the function score_game calculates the average number of attempts to guess the number

## Usage
The [guessnumber.ipynb](guessnumber.ipynb) file contains example of usage of the "Guess The Number" game.

```pythonregexp
import guessnumber
score_game(game_core_binary)
```

The result is:
```pythonregexp
Your algorithm guesses the number on average in 5 attempts
```