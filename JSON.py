import json

data = {
    "nom": "Jean",
    "age": 25,
    "ville": "Paris"
}

with open("data.json", "w") as file_JSON:
    json.dump(data, file_JSON, indent=2)

with open("data.json", "r") as file_JSON:
    Ajouter = json.load(file_JSON)
    print("Contenu du fichier initial :")
    print(Ajouter)


Ajouter["langage"] = "Python"

with open("data.json", "w") as file_JSON:
    json.dump(Ajouter, file_JSON, indent=2)

with open("data.json", "r") as file_JSON:
    Modifiez = json.load(file_JSON)
    print("\nContenu du fichier après modification :")
    print(Modifiez)