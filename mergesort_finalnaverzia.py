import random
from timeit import default_timer as timer

start = timer()

pole = random.sample(range(6000), 5000)

random.shuffle(pole)

print("Nezoradené pole je: ", pole)


def mergeSort(pole):
    if len(pole) > 1:

        mid = len(pole) // 2

        L = pole[:mid]

        R = pole[mid:]

        mergeSort(L)

        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                pole[k] = L[i]
                i += 1
            else:
                pole[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            pole[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            pole[k] = R[j]
            j += 1
            k += 1

mergeSort(pole)

end = timer()

print("Zoradenie trvalo: ", end - start, "sekúnd.")

print("Zoradené pole je: ",pole)