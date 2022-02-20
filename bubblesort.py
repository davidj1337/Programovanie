import random
from timeit import default_timer as timer

start = timer()

def bubbleSort(arr):
    n = len(pole)

    for i in range(n - 1):

        for j in range(0, n - i - 1):

            if pole[j] > pole[j + 1]:
                pole[j], pole[j + 1] = pole[j + 1], pole[j]


# Driver code to test above
pole = []
for i in range(0,5000):
    if random.randint(0,1):
        pole.append(i)

end = timer()

print("Zoradenie trvalo: ", end - start, "sekúnd.")

print("Nezoradený array je: ", pole)


print("Sorted array is:")
for i in range(len(pole)):
    print("% d" % pole[i], end=" ")