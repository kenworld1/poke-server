from flask import Flask, request, jsonify
import datetime, random

app = Flask(__name__)
clients = {}
pokes = []
event_log = []

def log(msg):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    line = f"[{timestamp}] {msg}"
    print(line)
    event_log.append(line)
    if len(event_log) > 100:
        event_log.pop(0)

@app.route("/")
def index():
    return "Serveur poke actif."

@app.route("/register/<id_client>", methods=["GET"])
def register(id_client):
    ip = request.remote_addr
    clients[id_client] = ip
    log(f"Connexion : ID={id_client} - IP={ip}")
    return jsonify({"status": "connecte", "id": id_client})

@app.route("/poke/<from_id>/<to_id>", methods=["GET"])
def poke(from_id, to_id):
    ip = clients.get(from_id, "unknown")
    pokes.append({"from": from_id, "to": to_id})
    log(f"POKE : from={from_id} ({ip}) -> to={to_id}")
    return jsonify({"status": "poke envoye", "from": from_id, "to": to_id})

@app.route("/getpokes/<id_client>", methods=["GET"])
def get_pokes(id_client):
    recu = [p for p in pokes if p["to"] == id_client]
    for p in recu:
        pokes.remove(p)
    return {"pokes": recu}

@app.route("/list_clients", methods=["GET"])
def list_clients():
    return jsonify(clients)

@app.route("/log", methods=["GET"])
def get_log():
    return jsonify(event_log)

@app.route("/help")
def help():
    return jsonify({
        "/register/<id>": "Enregistre un client",
        "/poke/<from>/<to>": "Envoie un poke",
        "/getpokes/<id>": "Recupere les pokes recus",
        "/list_clients": "Liste les clients connectes",
        "/log": "Retourne les logs d'evenement"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
