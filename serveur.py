from flask import Flask, request
import datetime

app = Flask(__name__)
clients = {}
pokes = []

@app.route('/')
def accueil():
    return "Serveur poke actif."

@app.route('/register/<id_client>', methods=['GET'])
def register(id_client):
    ip = request.remote_addr
    clients[id_client] = ip
    return f"Client {id_client} enregistre avec IP {ip}\n"

@app.route('/poke/<from_id>/<to_id>', methods=['GET'])
def poke(from_id, to_id):
    pokes.append({"from": from_id, "to": to_id})
    return f"Poke envoye de {from_id} vers {to_id}\n"

@app.route('/getpokes/<id_client>', methods=['GET'])
def get_pokes(id_client):
    recu = [p for p in pokes if p["to"] == id_client]
    for p in recu:
        pokes.remove(p)
    return {"pokes": recu}

# Interface texte retro simplifiee via console
def console():
    print("Console serveur active. Tape 'help' pour afficher l'aide.")
    while True:
        cmd = input(">").split()

        if not cmd:
            continue

        if cmd[0] == "help":
            print("Commandes disponibles:")
            print("clients                   : Afficher IDs et IP connectes")
            print("poke [from] [to]          : Envoyer poke immediat")
            print("quit                      : Quitter la console serveur")

        elif cmd[0] == "clients":
            print("Clients connectes:")
            for id_client, ip in clients.items():
                print(f"{id_client} => {ip}")

        elif cmd[0] == "poke":
            if len(cmd) == 3:
                pokes.append({"from": cmd[1], "to": cmd[2]})
                print(f"Poke envoye de {cmd[1]} vers {cmd[2]}")
            else:
                print("Usage: poke [from_id] [to_id]")

        elif cmd[0] == "quit":
            print("Fermeture console serveur.")
            break

        else:
            print("Commande inconnue. Tape 'help'.")

if __name__ == "__main__":
    from threading import Thread
    Thread(target=lambda: app.run(host='0.0.0.0', port=10000)).start()
    console()
