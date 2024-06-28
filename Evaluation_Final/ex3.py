import random 

with open("moyen.txt", "w") as fic :
    for i in range(random.randint(5, 100)):
        fic.write(str(random.randint(1, 1000)) + " ")


with open("moyen.txt", "r") as fic:
    nombres = fic.read()
    nombres = nombres.split(" ")
    longueur = len(nombres)
    total = 0
    for nombre in nombres :
        if nombre != "" :
            total += int(nombre)
    moyen = total / longueur

print(f"nombre de nombres : {longueur}")
print(f"la somme est : {total}")
print(f"la moyenne est : {round(moyen, 1)}")
