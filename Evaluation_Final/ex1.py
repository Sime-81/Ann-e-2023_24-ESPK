zen = ["Préfère :\n", "la beauté à la laideur,\n", "l'explicite à l'implicite,\n", "le simple au complexe"]

with open("zenPython.txt", "w") as fic:
    for a in zen:
        fic.write(a)

with open("zenPython.txt", "r") as fic:
    print(fic.read())
