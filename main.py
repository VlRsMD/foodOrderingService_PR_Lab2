from flask import Flask, request

food_ordering_server = Flask(__name__)

@food_ordering_server.route('/client', methods = ['GET', 'POST'])
def post():
    req = request.json
    return req

@food_ordering_server.route('/restaurant', methods = ['GET', 'POST'])
def get():
    req = request.json
    return req

if __name__ == '__main__':
    food_ordering_server.run(host='127.0.0.1', port=3800)
