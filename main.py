"""
class Numbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.current < self.limit:
            if self.current % 2 == 0:
                count_num = self.current
                self.current += 1
                return count_num
            self.current += 1
        raise StopIteration()

diapozon = Numbers(10)
for i in diapozon:
    print(i)
"""


"""
import random
def random_gen():
    actiocns = ["Випий води!","Зроби розминку", "Посміхнись","Пограй","Поїш","Поспи"]

    while True:
        choice = random.choice(actiocns)
        yield choice

viklik = random_gen()

print("Порада 1 ",next(viklik))
print("Порада 2 ",next(viklik))
print("Порада 3 ",next(viklik))
print("Порада 4 ",next(viklik))
print("Порада 5 ",next(viklik))
print("Порада 6 ",next(viklik))
"""

"""
# Замикання функції

def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

my_counter = counter()

print(my_counter())
"""
"""
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

my_counter = counter()

while True:
    print(my_counter())
"""

def decorator(func):
    def obgortka():
        print("----Щось відбувається до функції-----")
        func()
        print("----Щось відбувається після функції-----")
    return obgortka

@decorator
def say_hello():
    print("Хелло мабой! Ва ту ю ду?")

say_hello()




