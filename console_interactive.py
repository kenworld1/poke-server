import requests

url_serveur = "http://127.0.0.1:10000"

print("Console Poke active. Tape 'help' pour la liste des commandes.")
while True:
    commande = input("> ")

    if commande == 'help':
        print("""
        Commandes disponibles :
        clients              : liste les clients connectés
        poke [from] [to]     : envoie un poke d'un ID vers un autre
        quit                 : quitter
        """)
    elif commande == 'clients':
        r = requests.get(url_serveur + "/clients")
        if r.ok:
            clients = r.json()
            if clients:
                print("Clients connectés :")
                for id, ip in clients.items():
                    print(f"ID={id} IP={ip}")
            else:
                print("Aucun client connecté.")
        else:
            print("Erreur récupération des clients.")

    elif commande.startswith("poke"):
        _, from_id, to_id = commande.split()
        r = requests.post(url_serveur + "/poke", json={"from_id": from_id, "to_id": to_id})
        if r.ok:
            print(r.json()['status'])
        else:
            print("Erreur d'envoi du poke.")

    elif commande == 'quit':
        break

    else:
        print("Commande inconnue, tape 'help'.")
