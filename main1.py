import logging

logging.basicConfig(level=logging.INFO)


def fibonacci(i):
    fib1 = 1
    fib2 = 1
    j = 2
    if i in (1, 2):
        fib_sum = 1
    while j < i:
        fib_sum = fib2 + fib1
        fib1 = fib2
        fib2 = fib_sum
        j = j + 1
    return fib_sum


while True:
    try:
        m = int(input())
        res = fibonacci(m)
        logging.info("%s", res)
    except ValueError:
        logging.info("try again")
