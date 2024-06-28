fruits = ["pomme", "poire", "pêche"]

with open("fruits.txt", "w") as fic:
    for a in fruits:
        fic.write(a + "\n")


with open("nombres.txt", "w") as fic:
    for a in range(100):
        fic.write(str(a+1) + "\n")     