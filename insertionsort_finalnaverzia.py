import random
from timeit import default_timer as timer

start = timer()

pole = random.sample(range(6000), 5000)

random.shuffle(pole)

print("Nezoradený array je: ", pole)


def insertionSort(pole):
    for i in range(1, len(pole)):

        key = pole[i]

        j = i - 1
        while j >= 0 and key < pole[j]:
            pole[j + 1] = pole[j]
            j -= 1
        pole[j + 1] = key

insertionSort(pole)

end = timer()

print("Zoradenie trvalo: ", end - start, "sekúnd.")

print("Zoradené pole je: ",pole)