# Task 1


def caching_fibonacci():
    cache = {}

    def fibonacci(num: int) -> int:
        if num <= 0:
            return 0

        elif num == 1:
            return 1

        else:
            if num in cache:
                print(cache)
                return cache[num]

            cache[num] = fibonacci(num - 1) + fibonacci(num - 2)
            return cache[num]

    return fibonacci


fib = caching_fibonacci()

print(fib(10))
print(fib(15))
