#from flask_cors import CORS, cross_origin
from flask import Flask,render_template,send_from_directory,request, jsonify,make_response
#from flask_cors import CORS, cross_origin

app = Flask(__name__,static_folder='frontend/build',static_url_path='')

@app.route('/',methods=['GET'])
def base():
    return send_from_directory(app.static_folder,'index.html')


@app.route("/hello",methods=['GET'])
def hello():
    # return make_response(jsonify(hello))
    # return make_response(hello)
    return make_response(jsonify(hello="hello this is adithya"))




if __name__=="__main__":
    app.run(debug=True)