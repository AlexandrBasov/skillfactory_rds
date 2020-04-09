import numpy as np


def game_core_binary(number):
    """В основе данного метода лежит Бинарный поиск (также известен как метод деления пополам).
     Возможные варианты ответов представлены в виде упорядоченного массива variants."""
    count = 0
    variants = [x for x in range(1, 101)]
    start = 0
    end = len(variants)
    while start < end:
        count += 1
        middle = (start + end) // 2
        if number == variants[middle]:
            break
        if number <= variants[middle]:
            end = middle
        else:
            start = middle + 1
    return count  # выход из цикла, если угадали


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


# запускаем
score_game(game_core_binary)
