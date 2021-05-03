from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from .models import Company, Product, Recharge
from main import db

'''
    Criando argumentos de entrada para as empresas e produtos
    RequestParser() recebe os requests providos pelo test.py
'''

Company_args = reqparse.RequestParser()
Company_args.add_argument('company_id', type=str, required=True)

CompanyUpdate_args = reqparse.RequestParser()
CompanyUpdate_args.add_argument('company_id', type=str)

Recharge_args = reqparse.RequestParser()
Recharge_args.add_argument('id', type=str)
Recharge_args.add_argument('company_id', type=str)
Recharge_args.add_argument('product_id', type=str)
Recharge_args.add_argument('phone_number', type=int)
Recharge_args.add_argument('value', type=float)

company_fields = {
    'company_id': fields.String,
    'products': fields.Nested({
        'id': fields.String,
        'value': fields.Float
    })
}

recharge_fields = {
    'id': fields.String,
    'created_at': fields.String,
    'company_id': fields.String,
    'product_id': fields.String,
    'phone_number': fields.Integer,
    'value': fields.Float
}

class CompanyProducts(Resource):
    @marshal_with(company_fields)
    def get(self, company_id=None):

        '''
            Caso não seja passado o parâmetro 'company_id', o query mostra todas ocorrências
            Caso o parâmetro for encontrado, o query mostrará a primeira ocorrência
            Tratamento de erro: HTTP 404 - Mensagem: 'Empresa não encontrada'

        '''

        if not company_id:
            result = Company.query.all()
            return result
        result = Company.query.filter_by(company_id=company_id).first()
        if not result:
            abort(404, message="Empresa nao encontrada.")
        return result

    @marshal_with(company_fields)
    def put(self, company_id):

        '''
            Caso o parâmetro for encontrado, o query mostrará a primeira ocorrência
            Tratamento de erros:
                HTTP 409 - Mensagem: 'Empresa já existe'
                HTTP 201 - Mensagem: 'Criado com sucesso'

        '''

        company_args = Company_args.parse_args()
        result = Company.query.filter_by(company_id=company_id).first()

        if result:
            abort(409, message="Empresa ja existente.")

        company = Company(company_id=company_args['company_id'])
        db.session.add(company)
        db.session.commit()
        return company, 201 # HTTP 201: Criado com sucesso

    @marshal_with(company_fields)
    def patch(self, company_id):

        '''
            Encontra o parâmetro 'company_id' e atualiza as informações definidas
            Tratamento de erro: HTTP 404 - Mensagem: 'Empresa não encontrada'

        '''

        args = CompanyUpdate_args.parse_args()
        result = Company.query.filter_by(company_id=company_id).first()
        if not result:
            abort(404, message="Empresa nao encontrada.")
        if args['company_id']:
            result.company_id = args['company_id']
        db.session.commit()
        return result

    @marshal_with(company_fields)
    def delete(self, company_id):

        '''
            Encontra o parâmetro 'company_id' e deleta a primeira ocorrência
            Tratamento de erro:
                HTTP 404 - Mensagem: 'Empresa não encontrada'
                HTTP 204 - Mensagem: 'Excluído com sucesso'

        '''

        result = Company.query.filter_by(company_id=company_id).first()
        if not result:
            abort(404, message="Empresa nao encontrada.")

        db.session.delete(result)
        db.session.commit()
        return '', 204

class PhoneRecharge(Resource):
    @marshal_with(recharge_fields)
    def get(self, id=None):

        '''
            Caso não seja passado o parâmetro 'id' ou 'phone_number', o query mostra todas ocorrências
            Caso o parâmetro 'id' for encontrado, o query mostrará a primeira ocorrência
            Caso o parâmetro 'phone_number' for encontrado, o query mostrará todas ocorrências
            Tratamento de erro: HTTP 404 - Mensagem: 'Recarga não encontrada'

        '''


        if not id:
            result = Recharge.query.all()
            return result

        result = Recharge.query.filter_by(id=id).first()
        if result:
            result = Recharge.query.filter_by(id=id).first()
        else:
            result = Recharge.query.filter_by(phone_number=id).all()
        if not result:
            abort(404, message="Recarga nao encontrada.")
        return result

    @marshal_with(recharge_fields)
    def put(self, id):

        '''
            Caso o parâmetro for encontrado, o query mostrará a primeira ocorrência
            Verificações quando requisitado a recarga:
                Recarga com este id já foi realizada? (id)
                A empresa solicitada existe? (company_id)
                O produto disponibilizado pela empresa existe? (product_id)
            Tratamento de erros:
                HTTP 404 - Mensagem: 'Empresa ou produto não existe'
                HTTP 201 - Mensagem: 'Criado com sucesso'

        '''
        recharge_args = Recharge_args.parse_args()
        result = Recharge.query.filter_by(id=id).first()
        if result:
            abort(409, message="Recarga ja existente")
        company = Company.query.filter_by(company_id=recharge_args['company_id']).first()
        if not company:
            abort(404, message="Empresa nao encontrada.")
        product = Product.query.filter_by(id=recharge_args['product_id']).first()
        if not product:
            abort(404, message="Produto nao encontrado.")
        recharge = Recharge(id=id, company=company, product=product, phone_number=recharge_args['phone_number'], value=recharge_args['value'])
        db.session.add(recharge)
        db.session.commit()
        return '', 201 # HTTP 201: Criado com sucesso
