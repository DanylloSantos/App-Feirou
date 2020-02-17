from flask import Flask,jsonify,request

app = Flask(__name__)

# Importando controller dos produtos
from app.controllers import produtos