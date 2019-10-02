from flask import Flask, jsonify
from os import environ

app = Flask(__name__)

@app.route('/')
def root():
  return jsonify({ 'msg': 'It works!'})

app.run(host=environ['HOST'], port=environ['PORT'])
