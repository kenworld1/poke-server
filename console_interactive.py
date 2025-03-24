import requests

BASE = "http://localhost:10000"
history = []

def list_clients():
    r = requests.get(BASE + "/list_clients")
    print("Clients connectes :")
    for k, v in r.json().items():
        print(f"{k} => {v}")

def poke(from_id, to_id):
    r = requests.get(BASE + f"/poke/{from_id}/{to_id}")
    print(r.text)

def show_events():
    r = requests.get(BASE + "/log")
    print("\n".join(r.json()))

def help():
    print("Commandes disponibles :")
    print(" clients               : liste les clients")
    print(" poke [from] [to]      : poke vers un ID")
    print(" events                : afficher les evenements")
    print(" history               : historique local")
    print(" help                  : aide")
    print(" quit                  : quitter")

def run():
    print("Console Poke active. Tape 'help' pour la liste des commandes.")
    while True:
        try:
            cmd = input("> ").strip()
            if not cmd:
                continue
            history.append(cmd)
            parts = cmd.split()
            if parts[0] == "help":
                help()
            elif parts[0] == "clients":
                list_clients()
            elif parts[0] == "poke" and len(parts) == 3:
                poke(parts[1], parts[2])
            elif parts[0] == "events":
                show_events()
            elif parts[0] == "history":
                print("\n".join(history))
            elif parts[0] == "quit":
                print("Bye.")
                break
            else:
                print("Commande inconnue.")
        except Exception as e:
            print("Erreur :", e)

if __name__ == "__main__":
    run()
