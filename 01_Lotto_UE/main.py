import random


def lotto_numbers():
    numbers = list(range(1, 46))  # List of numbers from 1 to 45
    number_lotto = []  # List to store drawn numbers

    for i in range(6):
        random_index = random.randint(0, 44 - i)
        number_lotto.append(numbers[random_index])
        numbers[random_index], numbers[44 - i] = numbers[44 - i], numbers[random_index] # Swap drawn number with last number in list

    return number_lotto

def lotto_statistic():
    stats = {i: 0 for i in range(1, 46)}  # Initialize dictionary to count occurrences of each number

    for _ in range(1000):
        drawn_numbers = lotto_numbers()
        for numbers in drawn_numbers:
            stats[numbers] += 1

    return stats



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Lotto numbers: ", lotto_numbers())
    statistics = lotto_statistic()
    for number, count in statistics.items():
        print(f"Number {number}: {count} times")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
