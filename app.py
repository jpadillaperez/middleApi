from flask import Flask, jsonify
from pymongo import MongoClient

# Load the environment variables from the .env.local file
#from dotenv import load_dotenv
#load_dotenv('.env.local')

# Access the environment variable by its name
#MONGODB_URI = os.environ['MONGODB_URI']

app = Flask(__name__)

#client = MongoClient(MONGODB_URI)
client = MongoClient(
    "mongodb+srv://jorge:jorge@tpt.tw8tdw7.mongodb.net/?retryWrites=true&w=majority")

db = client["tpt"]
collection = db["beaches"]


@app.route('/api/python/getRandomID')
def getRandomID():
    random_doc = collection.aggregate([{'$sample': {'size': 1}}]).next()
    random_id = str(random_doc['_id'])
    return jsonify({'id': random_id})


@app.route('/api/python/getRecommendation')
def getRecommendation():
    return jsonify({'id_1': '64382e7a7d3c47097750ea10', 'id_2': '64382e7a7d3c47097750ea10'})


if __name__ == '__main__':
    app.run(host="0.0.0.0")
