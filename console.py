import requests

BASE = "http://localhost:10000"

def help():
    r = requests.get(BASE + "/help")
    print(r.text)

def list_clients():
    r = requests.get(BASE + "/list_clients")
    print(r.text)

def poke(from_id, to_id):
    r = requests.get(BASE + f"/poke/{from_id}/{to_id}")
    print(r.text)
