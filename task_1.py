import queue
import random
import time

queue = queue.Queue()

def generate_request() -> None:
    request_count = random.randint(1, 10)
    for i in range(request_count):
        queue.put(f"Request: {i}")
        print(f"Створено заявку: {i}")
        

def process_request() -> bool:
    if not queue.empty():
        request_id = queue.get()
        print(f"Обробка заявки: {request_id}")
        return True
    else:
        print("Черга пуста")
        return False

try:
    while True:
        generate_request()
        # Виклик функції для обробки заявок
        while process_request():
            pass
        # Імітація затримки між операціями
        time.sleep(10)

except KeyboardInterrupt:
    print("Вихід з програми.")