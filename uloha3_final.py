vysledky = input("Zadajte výsledky zápasov: ")
Ty = input("Zadaj svoje tipy: ")
ty_list = list (map(int,Ty.split()))
tymy = [int(i) for i in vysledky if i.isdigit()]
pocet_zapasov = len(tymy) // 2
Jano = [6,5,8]
Tomas = [2,8,9]
Peter = [7,9,8,12]
vstup = ""

for i in range(1,(pocet_zapasov+1)*2):
    if i > pocet_zapasov*2:
        break
    elif i % 2 == 0:
        pass
    else:
            zapas = tymy[i-1] + tymy[i]
            zapas = str(zapas)
            vstup = vstup + zapas + " "

int_list = list (map(int,vstup.split()))


pocet1 = set(int_list)&set(Jano)
str_pocet1 = " ".join(map(str,pocet1))
pocet_st1 = len(pocet1)


pocet2 = set(int_list)&set(Tomas)
str_pocet2 = " ".join(map(str,pocet2))
pocet_st2 = len(pocet2)


pocet3 = set(int_list)&set(Peter)
str_pocet3 = " ".join(map(str,pocet3))
pocet_st3 = len(pocet3)

pocet4 = set(int_list)&set(ty_list)
str_pocet4 = " ".join(map(str,pocet4))
pocet_st4 = len(pocet4)

print("Futbalové výsledky:",vysledky)
print("Počet strelených gólov v zápase:",vstup)
print("Tipy súťažiacich:","Jano trafil:",str_pocet1,"Tomáš trafil:",str_pocet2,"Peter trafil:",str_pocet3,"Ty si trafil:",str_pocet4)
#Jeden má najviac
if pocet_st1 > pocet_st2 and pocet_st1 > pocet_st3 and pocet_st1 > pocet_st4:
    print("Najlepšie triafal Jano:",pocet_st1,"uhádnuté čísla")
elif pocet_st2 > pocet_st1 and pocet_st2 > pocet_st3 and pocet_st2 > pocet_st4:
    print("Najlepšie triafal Tomáš:",pocet_st2,"uhádnuté čísla")
elif pocet_st3 > pocet_st1 and pocet_st3 > pocet_st2 and pocet_st3 > pocet_st4:
    print("Najlepšie triafal Peter:",pocet_st3,"uhádnuté čísla")
elif pocet_st4 > pocet_st1 and pocet_st4 > pocet_st2 and pocet_st4 > pocet_st3:
    print("Najlepšie si triafal ty:",pocet_st4,"uhádnuté čísla")
elif pocet_st1 < 1 and pocet_st2 < 1 and pocet_st3 < 1 and pocet_st4 < 1:
    print("Nikto netrafil ani 1 zápas.")
elif pocet_st1 == pocet_st2 and pocet_st1 > pocet_st3 and pocet_st1 > pocet_st4:
    print("Najlepšie triafal Jano a Tomáš:",pocet_st1,"správnych tipov")
elif pocet_st1 == pocet_st3 and pocet_st1 > pocet_st2 and pocet_st1 > pocet_st4:
    print("Najlepšie triafal Jano a Peter:",pocet_st1,"správnych tipov")
elif pocet_st1 == pocet_st4 and pocet_st1 > pocet_st3 and pocet_st1 > pocet_st2:
    print("Najlepšie triafal Jano a ty:",pocet_st1,"správnych tipov")
elif pocet_st2 == pocet_st3 and pocet_st2 > pocet_st1 and pocet_st2 > pocet_st4:
    print("Najlepšie triafal Tomáš a Peter:",pocet_st2,"správnych tipov")
elif pocet_st2 == pocet_st4 and pocet_st2 > pocet_st3 and pocet_st2 > pocet_st1:
    print("Najlepšie triafal Tomáš a ty:",pocet_st2,"správnych tipov")
elif pocet_st3 == pocet_st4 and pocet_st3 > pocet_st2 and pocet_st3 > pocet_st1:
    print("Najlepšie triafal Peter a ty:",pocet_st3,"správnych tipov")
elif pocet_st1 == pocet_st2 and pocet_st1 == pocet_st3 and pocet_st1 > pocet_st4:
    print("Najlepšie triafal Jano, Tomáš a Peter:",pocet_st1,"správnych tipov")
elif pocet_st1 == pocet_st2 and pocet_st1 == pocet_st4 and pocet_st1 > pocet_st3:
    print("Najlepšie triafal Jano, Tomáš a ty:",pocet_st1,"správnych tipov")
elif pocet_st1 == pocet_st4 and pocet_st1 == pocet_st3 and pocet_st1 > pocet_st2:
    print("Najlepšie triafal Jano, Peter a ty:",pocet_st1,"správnych tipov")
elif pocet_st4 == pocet_st2 and pocet_st4 == pocet_st3 and pocet_st4 > pocet_st1:
    print("Najlepšie triafal Tomáš, Peter a ty:",pocet_st4,"správnych tipov")
else:
    print("Všetci trafili rovnaký počet zápasov:",pocet_st1,"správnych tipov")