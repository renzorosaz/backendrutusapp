#from sqlalchemy.sql.expression import select
from ..database import Session
from flask_restful import Resource
from sqlalchemy.sql.expression import select
from ..models.negocioturistico import NegocioTuristico
from flask import request
from flask import jsonify

class NegocioTurisController(Resource):

        
    # listar negocios turis
    def get(self):
        #negociosturisticos = select(NegocioTuristico)
        listar_negocios= NegocioTuristico.query.all()
        return jsonify(json_list =listar_negocios)
        #return jsonify(listar_negocios)


    def create_negocioturistico(self):
        session = Session()
        
        # play game
        data =request.json

        # instanciando clase model
        negocioturistico = NegocioTuristico()

        negocioturistico.ruc= data['ruc'],
        negocioturistico.nombre_anfitrion=data['nombre_anfitrion']
        negocioturistico.numero_contacto =data['numero_contacto']
        negocioturistico.departamento=data['departamento']
        
        session.add(negocioturistico)
        session.commit()
        #nuevo_negocio =NegocioTuristico(ruc,nombre_anfitrion,numero_contacto,departamento)
        # db.session.add(nuevo_negocio)
        # db.session.commit()

        print(negocioturistico)
        return "ok",201
       # return "Se registro correctamente el negocio turísitico",negocioturistico.jsonify(),201