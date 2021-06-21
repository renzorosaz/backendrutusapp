#from sqlalchemy.sql.expression import select
from ..database import Session
from flask_restful import Resource
from sqlalchemy.sql.expression import select
from ..models.negocioturistico import NegocioTuristico,NegocioTuristicoSchema

from flask import request


class NegocioTurisController(Resource):

    def get():
      negocios = NegocioTuristico.query.order_by(NegocioTuristico.ruc).all()
      negociosturisticos_schema = NegocioTuristicoSchema(many=True)
      print(negociosturisticos_schema)
      return negociosturisticos_schema.dump(negocios).data
        
    #listar negocios turis
    # def get(self):
    #     #ession = Session()
    #     negociosturisticos = db.session.query(NegocioTuristico).all()
    #     result = negociosturisticos_schema.dump(negociosturisticos)
    #     return jsonify(result.data)
      #  negociosturisticos = select(NegocioTuristico)
      
        #negociosturisticos = session.query(NegocioTuristico).all()
        # print('\n### All negocios:')
        # for negocioturistico in negociosturisticos:
        #     print(f'{negocioturistico.ruc}')
        #listar_negocios= NegocioTuristico.query.all()
        #return jsonify(json_list =listar_negocios)
       # employeeJSONData = json.dumps(negociosturisticos)
        #employeeJSON = json.loads(negociosturisticos)
        #return employeeJSON
    
    # def get(self):
    #     session = Session()
        
    #     data=request.json
    #     negocioturistencontrado= NegocioTuristico.query.filter_by(idnegocio_turistico=data).first()
        
    #     session.findall(negocioturistencontrado)
    #     session.commit()

    #     #print(negocioturistencontrado.data)
        
    #     return "no encontro"

   #def put(self):
        
        #idnegocio_turistico =request.json

        #negociosturisticos = select(NegocioTuristico)

        #data = NegocioTuristico.query.get(idnegocio_turistico)

    def post(self):
        session = Session()
        
        # play game
        data =request.json

        # instanciando clase model
        negocioturistico = NegocioTuristico()

        negocioturistico.ruc= data['ruc'],
        negocioturistico.nombre_anfitrion= data['nombre_anfitrion']
        negocioturistico.numero_contacto = data['numero_contacto']
        negocioturistico.departamento= data['departamento']
        
        session.add(negocioturistico)
        session.commit()
        #nuevo_negocio =NegocioTuristico(ruc,nombre_anfitrion,numero_contacto,departamento)
        # db.session.add(nuevo_negocio)
        # db.session.commit()

        print(negocioturistico.ruc)
        #return "ok",201
        return "Se registro correctamente el negocio turísitico",201
    