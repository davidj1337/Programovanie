import random
from timeit import default_timer as timer

start = timer()

pole = random.sample(range(20), 10)

random.shuffle(pole)

print("Nezoradený array je: ", pole)

def bubbleSort(pole):
    n = len(pole)

    for i in range(n - 1):

        for j in range(0, n - i - 1):

            if pole[j] > pole[j + 1]:
                pole[j], pole[j + 1] = pole[j + 1], pole[j]

bubbleSort(pole)

end = timer()

print("Zoradenie trvalo: ", end - start, "sekúnd.")

print("Zoradené pole je: ",pole)