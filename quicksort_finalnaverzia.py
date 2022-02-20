import random
from timeit import default_timer as timer

start = timer()

pole = random.sample(range(6000), 5000)

random.shuffle(pole)

print("Nezoradené pole je: ", pole)


def partition(pole, low, high):
    i = (low - 1)
    pivot = pole[high]

    for j in range(low, high):

        if pole[j] <= pivot:
            i = i + 1
            pole[i], pole[j] = pole[j], pole[i]

    pole[i + 1], pole[high] = pole[high], pole[i + 1]
    return (i + 1)


def quickSort(pole, low, high):
    if len(pole) == 1:
        return pole
    if low < high:

        pi = partition(pole, low, high)

        quickSort(pole, low, pi - 1)
        quickSort(pole, pi + 1, high)

n = len(pole)
quickSort(pole, 0, n-1)

end = timer()

print("Zoradenie trvalo: ", end - start, "sekúnd.")

print("Zoradené pole je: ",pole)