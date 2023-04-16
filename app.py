from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

#client = MongoClient("mongodb+srv://jorge:jorge@tpt.tw8tdw7.mongodb.net/?retryWrites=true&w=majority")
client = MongoClient("mongodb://root:example@192.168.1.30/?retryWrites=true&w=majority")
db = client["tpt"]
collection = db["natural_pools"]

@app.route('/api/python/getRandomID')
def getRandomID():
    random_doc = collection.aggregate([{'$sample': {'size': 1}}]).next()
    random_id = str(random_doc['_id'])
    return jsonify({'id': random_id})

@app.route('/api/python/getRecommendation')
def getRecommendation():
    return jsonify({'id_1': '64382e7a7d3c47097750ea10', 'id_2': '64382e7a7d3c47097750ea10'})

if __name__ == '__main__':
    app.run()
