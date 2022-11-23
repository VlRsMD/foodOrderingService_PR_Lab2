import requests
import json
import order_from_client
import order_from_restaurant

stack_client = []
stack_restaurant = []

def order_from_client():
    global stack_client
    receive = requests.get("http://127.0.0.1:3800/client")
    rec_order = json.loads(receive, object_hook=order_from_client.orderCl)
    ## add received order to stack
    stack_client.append(rec_order)

def order_to_restaurant():
    global stack_client
    l = len(stack_client)
    while l >= 0:
        order = stack_client.pop()
        order_to_json = json.dumps(order.__dict__)
        ## send new order to restaurant
        requests.post('http://127.0.0.1:3900/post', json=order_to_json)

def order_from_restaurant():
    global stack_restaurant
    receive = requests.get("http://127.0.0.1:3800/restaurant")
    rec_order = json.loads(receive, object_hook=order_from_restaurant.orderRest)
    ## add received order to stack
    stack_restaurant.append(rec_order)

def order_to_restaurant():
    global stack_restaurant
    l = len(stack_restaurant)
    while l >= 0:
        order = stack_client.pop()
        order_to_json = json.dumps(order.__dict__)
        ## send prepared order to client
        requests.post('http://127.0.0.1:3700/post', json=order_to_json)