import time
import random
import queue

def generate_request(request_queue, request_body, request_id):
    request_data = f"Request# {request_id} - {request_body}"
    if random.random() > 0.5:
        request_queue.put(request_data)
        print(f"New request {request_data}")
        time.sleep(2)
        return i + 1
    return i 

def process_request(request_queue):
    if not request_queue.empty():
        request_data = request_queue.get()
        print(f"Complited request {request_data}")
        time.sleep(2)
    else:
        print(f"Queue is empty")

possible_request = ["Sergii", "Oleh", "Bogdan", "Anna", "Olena"]

i = 0
q = queue.Queue()

try:
    while True:
        i = generate_request(q, random.choice(possible_request), i)
        process_request(q)
except:
    print("Stopped")
