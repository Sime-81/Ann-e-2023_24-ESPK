import json 

with open("test.Json", "w") as fichierJson :
    x = {"name": "John", "age": 30, "city": "New York"}

    fichierJson.write(json.dumps(x))

with open("test.Json", "r") as fic :
    a = json.loads(fic.read())
    print(type(a))

user = input("Catégorie : ")

try :
    print(f"Résultat dans Catégorie : \n({user} : {a[user.lower()]}) ")
except :
    print(f"Catégorie {user} inexistante")

