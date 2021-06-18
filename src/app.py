from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from decimal import Decimal
from datetime import datetime
from sqlalchemy.dialects.mysql import LONGTEXT
from flask_restful import Api

from .controllers.negocioturistico_controller import NegocioTurisController 

app = Flask(__name__)
api= Api(app)
#app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:030115lol@localhost/rutusbd'
#app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False


# db = SQLAlchemy(app)
# ma= Marshmallow(app)


api.add_resource(NegocioTurisController,'/negocioturistico')

#MODELO DE NEGOCIO TURISTICO
# class NegocioTuristico(db.Model):
#     idnegocio_turistico = db.Column(db.Integer,primary_key=True)
#     ruc =db.Column(db.String(45),unique=True)
#     nombre_anfitrion=db.Column(db.String(45))
#     numero_contacto =db.Column(db.String(45))
#     departamento =db.Column(db.String(45))

#     def __init__(self,ruc,nombre_anfitrion,numero_contacto,departamento):
#         self.ruc=ruc,
#         self.nombre_anfitrion=nombre_anfitrion,
#         self.numero_contacto=numero_contacto,
#         self.departamento=departamento

# class NegocioTuristicoSchema(ma.Schema):
#     class Meta:
#         fields =('idnegocio_turistico','ruc','nombre_anfitrion','numero_contacto','departamento')

# negocioturistico_schema = NegocioTuristicoSchema()
# negociosturisticos_schema = NegocioTuristicoSchema(many=True)

# @app.route('/negocioturist',methods=['POST'])
# def create_negocioturistico():
    
#     print(request.json)
#     ruc= request.json['ruc'],
#     nombre_anfitrion=request.json['nombre_anfitrion']
#     numero_contacto =request.json['numero_contacto']
#     departamento=request.json['departamento']

#     nuevo_negocio =NegocioTuristico(ruc,nombre_anfitrion,numero_contacto,departamento)
#     db.session.add(nuevo_negocio)
#     db.session.commit()

#     return negocioturistico_schema.jsonify(nuevo_negocio)

# @app.route('/listarnegociosturist',methods=['GET'])
# def get_negociosturis():
#     listar_negocios= NegocioTuristico.query.all()
#     result = negociosturisticos_schema.dump(listar_negocios)

#     return jsonify(result)

# @app.route('/buscarnegocioturist/<idnegocio_turistico>',methods=['GET'])
# def buscar_negocioturist(idnegocio_turistico):
#     negocio_encontrado = NegocioTuristico.query.get(idnegocio_turistico)
#     return negocioturistico_schema.jsonify(negocio_encontrado)

# @app.route('/negocioturist/<idnegocio_turistico>',methods=['PUT'])
# def actualizar_negocioturist(idnegocio_turistico):
#     negocio_encontrado = NegocioTuristico.query.get(idnegocio_turistico)
    
#     ruc= request.json['ruc'],
#     nombre_anfitrion=request.json['nombre_anfitrion']
#     numero_contacto =request.json['numero_contacto']
#     departamento=request.json['departamento']

#     negocio_encontrado.ruc= ruc
#     negocio_encontrado.nombre_anfitrion= nombre_anfitrion
#     negocio_encontrado.numero_contacto = numero_contacto
#     negocio_encontrado.departamento= departamento

#     db.session.commit()
#     return negocioturistico_schema.jsonify(negocio_encontrado)

# @app.route('/eliminarnegocio/<idnegocio_turistico>',methods=['DELETE'])
# def eliminar_negocioturis(idnegocio_turistico):
#     negocio_encontrado = NegocioTuristico.query.get(idnegocio_turistico)
#     db.session.delete(negocio_encontrado)
#     db.session.commit()

#     return negocioturistico_schema.jsonify(negocio_encontrado)


# #MODELO de REGION
# class Region(db.Model):
#     idregion =db.Column(db.Integer,primary_key=True)
#     nombre_region=db.Column(db.String)


# #MODELO DE USUARIO
# class Usuario(db.Model):
#     idusuario = db.Column(db.Integer,primary_key=True)
#     ruc =db.Column(db.String(45),unique=True)
#     nombre_anfitrion=db.Column(db.String(45))
#     numero_contacto =db.Column(db.String(45))
#     departamento =db.Column(db.String(45))

# #MODELO DE EXCURSION
#     idexcursion=db.Column(db.Integer,primary_key=True)
#     #regiones=db.relationship('Region',backref='region')
#     idregion=db.Column(db.Integer,db.ForeignKey('region.idregion'))
#     foto_portada=db.Column(db.String(255))
#     nombre_excursion=db.Column(db.String(255))
#     descripcion= db.Column(db.TEXT(20000000))
#     duracion=db.Column(db.String(25))
#     precio=db.Column(db.Numeric)
#     departamento = db.Column(db.String(45))
#     medio_pago=db.Column(db.String(45))
#     fecha_inicio=db.Column(db.DATE)
#     fecha_fin=db.Column(db.DATE)
#     aforo= db.Column(db.Integer)
#     incluye=db.Column(db.String(255))
#     no_incluye=db.Column(db.String(255))
#     idnegocio_turistico=db.Column(db.Integer,db.ForeignKey('negocio_turistico.idnegocio_turistico'))

# #MODELO DE SOLICITUD DE RESERVA


# #MODELO DE ITINERARIO



if __name__ == '__main__':
    app.run(debug=True)


# @app.route('/',methods =['GET'])
# def index():
#     return jsonify({"message":"bienvenido a mi api"})