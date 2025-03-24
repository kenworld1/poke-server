import requests

server = "https://poke-server-1.onrender.com"
print("Console Poke active. Tape 'help' pour la liste des commandes.")

while True:
    cmd = input("> ")
    if cmd == "quit":
        break
    elif cmd == "help":
        print("clients : liste les clients connectes")
        print("poke ID : poke le client avec l'ID indiqué")
        print("quit : quitter la console")
    elif cmd == "clients":
        response = requests.get(f"{server}/clients")
        print(response.json())
    elif cmd.startswith("poke "):
        _, id = cmd.split()
        response = requests.get(f"{server}/poke/{id}")
        if response.ok:
            print(f"Client {id} poke avec succès.")
        else:
            print("Erreur lors du poke.")
    else:
        print("Commande inconnue.")
