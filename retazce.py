def pocet_suborov():
    while True:
        odpoved = input("Zadaj počet súborov: ")
        if int(odpoved):
            return int(odpoved)
        else:
            print("To nebolo číslo!")


input2 = []
poradie_slova = 0

with open("basnicka.txt", encoding="utf-8") as subor:
    for riadok in subor:
        input2 += riadok.split()

for i in range(pocet_suborov()):
    poradie_slova += 1
    if poradie_slova == len(input2):
        poradie_slova -= len(input2)
    with open(f"""slovo{poradie_slova}""", mode="w", encoding="utf-8") as subor:
        print(input2[poradie_slova - 1], file=subor)