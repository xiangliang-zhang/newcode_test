import random

def get_k():
    return max(random.random(), random.random())

def answer():
    i = 10000000
    x = 0.6
    count = 0
    for item in range(i):
        if get_k() < x:
            count += 1
    return count / i

print(answer())