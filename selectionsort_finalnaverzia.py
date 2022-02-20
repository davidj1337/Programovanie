import sys
import random
from timeit import default_timer as timer

start = timer()


pole = random.sample(range(6000), 5000)

random.shuffle(pole)

print("Nezoradené pole je: ", pole)

for i in range(len(pole)):

    min_idx = i
    for j in range(i + 1, len(pole)):
        if pole[min_idx] > pole[j]:
            min_idx = j

    pole[i], pole[min_idx] = pole[min_idx], pole[i]

end = timer()

print("Zoradenie trvalo: ", end - start, "sekúnd.")


print("Zoradené pole je:", pole)
