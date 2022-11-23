import requests
import json
from types import SimpleNamespace

stack_restaurant = []

def order_from_restaurant():
    global stack_restaurant
    receive = requests.get("http://127.0.0.1:3800/restaurant")
    rec_order = json.loads(receive.json(), object_hook=lambda d: SimpleNamespace(**d))
    ## add received order to stack
    stack_restaurant.append(rec_order)
    print(receive.json())

def order_to_client():
    global stack_restaurant
    l = len(stack_restaurant)
    while l >= 0:
        order = stack_restaurant.pop()
        order_to_json = json.dumps(order.__dict__)
        ## send prepared order to client
        send = requests.post('http://127.0.0.1:3700/post', json=order_to_json)
        print(send.json())

print('List of orders received from the restaurant: ')
order_from_restaurant()
print('List of orders sent to the client: ')
order_to_client()