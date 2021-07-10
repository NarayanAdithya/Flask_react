from flask import Flask,render_template,send_from_directory,request, jsonify,make_response
from flask_cors import CORS, cross_origin
from app import app
@app.route('/',methods=['GET'])
@app.route("/hello",methods=['GET'])
def hello():
    # return make_response(jsonify(hello))
    # return make_response(hello)
    return make_response(jsonify(hello="hello this is adithya"))
