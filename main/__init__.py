from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

# Encontrando os arquivos do projeto
app = Flask(__name__)

# Configuração da SECRET_KEY
app.config['SECRET_KEY'] = '873429eaf1526c737bb32dcb6405f291'

# Configuração do SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app) # Conectando a database ao aplicativo

# Configuração do Api
from .api import CompanyProducts, PhoneRecharge
from main import routes

api = Api(app)
api.add_resource(CompanyProducts, '/CompanyProducts/', '/CompanyProducts/<string:company_id>')
api.add_resource(PhoneRecharge, '/PhoneRecharges/', '/PhoneRecharges/<string:id>')
