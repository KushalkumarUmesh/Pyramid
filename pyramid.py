from flask import Flask
app = Flask(__name__)

import requests
from flask import jsonify


app.rout("/ping",methods=['POST'])
def func1():
    body=requests.get_json()
    payload=(body.url,'GET')
    requests.get(payload)
    return payload

app.route("/info",methods=['GET'])
def func2():
    data = {
			'status' : 'Receiver',
			'msg' : 'Cisco is the best!'
		}
    return jsonify(data)   
