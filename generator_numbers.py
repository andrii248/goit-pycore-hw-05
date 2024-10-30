# Task 2

from typing import Callable
import re


def generator_numbers(text: str):
    pattern = r"(?<=\s)\d+(?:\.\d*)?(?=\s)"
    results = re.findall(pattern, text)
    for number in results:
        yield float(number)


def sum_profit(text: str, func: Callable):
    total = 0
    incomes = func(text)
    for income in incomes:
        total += income

    return total


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
