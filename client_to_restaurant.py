import requests
import json
from types import SimpleNamespace

stack_client = []

def order_from_client():
    global stack_client
    receive = requests.get('http://127.0.0.1:3800/client')
    rec_order = json.loads(receive.json(), object_hook=lambda d: SimpleNamespace(**d))
    ## add received order to stack
    stack_client.append(rec_order)
    print(receive.json())

def order_to_restaurant():
    global stack_client
    l = len(stack_client)
    while l >= 0:
        order = stack_client.pop()
        order_to_json = json.dumps(order.__dict__)
        ## send new order to restaurant
        send = requests.post('http://127.0.0.1:3900/post', json=order_to_json)
        print(send.json())

print('List of orders received from the client: ')
order_from_client()
print('List of orders sent to the restaurant: ')
order_to_restaurant()