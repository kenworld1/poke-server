import requests

BASE = "http://localhost:10000"

def list_clients():
    r = requests.get(BASE + "/list_clients")
    print("Clients connectes :")
    for k, v in r.json().items():
        print(f"{k} => {v}")

def poke(from_id, to_id):
    r = requests.get(BASE + f"/poke/{from_id}/{to_id}")
    print(r.text)

def help():
    print("Commandes disponibles :")
    print(" clients              : liste tous les clients")
    print(" poke [from] [to]     : poke un ID vers un autre")
    print(" help                 : affiche cette aide")
    print(" quit                 : quitter la console")

def run():
    print("Console Poke active. Tape 'help' pour la liste des commandes.")
    while True:
        try:
            cmd = input("> ").strip().split()
            if not cmd:
                continue
            if cmd[0] == "help":
                help()
            elif cmd[0] == "clients":
                list_clients()
            elif cmd[0] == "poke" and len(cmd) == 3:
                poke(cmd[1], cmd[2])
            elif cmd[0] == "quit":
                print("Bye.")
                break
            else:
                print("Commande inconnue.")
        except Exception as e:
            print("Erreur :", e)

if __name__ == "__main__":
    run()
