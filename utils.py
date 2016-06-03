from math import sqrt

def fibo_generator():
    n_1 = 1
    n_2 = 1
    yield n_2
    yield n_1
    while True:
        n = n_2 + n_1
        yield n
        n_2 = n_1
        n_1 = n

def prime(number):
    return len(factors(number)) == 2

def prime_generator():
    number = 1
    while True:
        while not prime(number):
            number += 1
        yield number
        number += 1

def factors(number):
    max_factor = int(sqrt(number)) + 1
    answer = []
    a = 1
    while a < max_factor:
        if number % a == 0:
            answer.append(a)
            b = number / a
            if b != a:
                answer.append(b)
        a += 1
    answer.sort()
    return answer