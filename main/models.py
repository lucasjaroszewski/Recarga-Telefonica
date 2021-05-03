from datetime import datetime
from main import db

# Definindo modelos da database
class Company(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.String(10), nullable=False)

class Product(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    id = db.Column(db.String(10), nullable=False)
    company_id = db.Column(db.String(10), db.ForeignKey('company.pk'))
    company = db.relationship('Company', backref='products', lazy='select')

class Recharge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    phone_number = db.Column(db.Integer)
    value = db.Column(db.Float)
    company_id = db.Column(db.String(10), db.ForeignKey('company.company_id'))
    company = db.relationship('Company', backref='rechargesC', lazy='select')
    product_id = db.Column(db.String(10), db.ForeignKey('product.id'))
    product = db.relationship('Product', backref='rechargesP', lazy='select')

db.create_all()
