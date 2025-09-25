import time
import requests

def do_work():
    print("Worker is running...")
    while True:
        # Qui puoi aggiungere la logica del tuo worker
        # Per ora simula solo un'attività
        print("Worker heartbeat: still alive")
        time.sleep(10)

if __name__ == "__main__":
    do_work()
