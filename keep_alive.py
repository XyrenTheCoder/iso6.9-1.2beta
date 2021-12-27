from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "totally not online"

def run():
    app.run(host="0.0.0.0", port=6969)

def keep_alive():
    s = Thread(target=run)
    s.start() 
