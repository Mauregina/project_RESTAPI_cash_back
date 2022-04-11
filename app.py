from flask import Flask, jsonify
from flask_restful import Api
from resources.customer import Customer, Customers
from resources.sale import Sales, Sale


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def cria_banco():
    banco.create_all()    

api.add_resource(Customers, '/customers')
api.add_resource(Customer, '/customer/<int:document>')
api.add_resource(Sales, '/sales')
api.add_resource(Sale, '/api/cashback')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)