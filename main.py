from flask import Flask, request

food_ordering_server = Flask(__name__)

@food_ordering_server.route('/client', methods = ['GET','POST'])
def cl():
    req1 = request.json
    return req1

@food_ordering_server.route('/restaurant', methods = ['GET','POST'])
def rest():
    req1 = request.json
    return req1

if __name__ == '__main__':
    food_ordering_server.run(host='127.0.0.1', port=3800)
