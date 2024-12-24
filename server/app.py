from models import db,Images,Product
from flask_migrate import Migrate
from flask import Flask,request,make_response,jsonify
from flask_restful import Api,Resource
from flask_cors import CORS
import cloudinary
import cloudinary.uploader
import cloudinary.api
import os,json


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app=Flask(__name__)
CORS(app)
migrate=Migrate(app,db)
api=Api(app)

cloudinary.config(
    cloud_name="dia2le5vz",
    api_key="716219668214133",
    api_secret="12Wn1cP9Wc_cZb6gFWMe2tdvHWQ"
)