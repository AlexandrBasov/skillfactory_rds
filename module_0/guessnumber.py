import numpy as np


def game_core_binary(number):
    """To guess a number we implement a binary search algorithm."""

    variants = [x for x in range(1, 101)]  # All possible answers from 1 to 100

    attempts = 0  # counter for number of attempts
    left = 0
    right = len(variants)

    while left < right:
        attempts += 1
        middle = (left + right) // 2
        if number == variants[middle]:
            break
        if number <= variants[middle]:
            right = middle
        else:
            left = middle + 1

    return attempts


def score_game(game_core):
    """Run the game 1000 times to find out how fast the game guesses
     number"""

    results_list = []

    # fix RANDOM SEED so that your experiment is reproducible!
    np.random.seed(1)

    random_numbers = np.random.randint(1, 101, size=1000)

    for number in random_numbers:
        results_list.append(game_core(number))

    average_attempts = int(np.mean(results_list))

    print(f"Your algorithm guesses the number on average in {average_attempts} attempts")
    return average_attempts


# run the game
score_game(game_core_binary)
