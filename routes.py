#este modulo toma cuidado de comenzar el API Server , cargando el db y comenzando los enpoints  
import os
from flask import Flask,request, jsonify, url_for, Blueprint 
from api.models import db,User 
from api.utils import generate_sitemaps, APIException 
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


#create flask app
api=Blueprint["api",__name__]
app.config["JWT_SECRET_KEY"] = os.getENV('JWT_SECRET')  # Change this!
jwt = JWTManager(app)


#create una ruta para autenticar usuarios y retornar jwt 
#create_access_token , funcion usada para generar el JWT
@app.route("/token", methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if email != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)
    return jsonify(response_body),200
