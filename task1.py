import queue
import time
import random

queue = queue.Queue()

def generate_request():
    request_number = random.randint(1, 1000)
    queue.put(request_number)
    print(f"Заявка {request_number} була додана до черги.")

def process_request():
    if not queue.empty():
        request_number = queue.get()
        print(f"Заявка {request_number} була оброблена.")
    else:
        print("Черга порожня. Немає заявок для обробки.")

while True:
    generate_request()
    generate_request()
    process_request()
    time.sleep(1)
