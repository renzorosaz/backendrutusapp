from flask import Flask,jsonify,request
from decimal import Decimal
from datetime import datetime
from sqlalchemy.dialects.mysql import LONGTEXT
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#from .controllers.negocioturistico_controller import NegocioTurisController

app = Flask(__name__)
api= Api(app)
db = SQLAlchemy(app)
ma= Marshmallow(app)

app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:030115lol@localhost/rutusbd'



#api.add_resource(NegocioTurisController,'/negocioturistico')

#MODELO DE NEGOCIO TURISTICO
class NegocioTuristico(db.Model):
    idnegocio_turistico = db.Column(db.Integer,primary_key=True)
    ruc =db.Column(db.String(45),unique=True)
    nombre_anfitrion=db.Column(db.String(45))
    numero_contacto =db.Column(db.String(45))
    departamento =db.Column(db.String(45))
    idusuario=db.Column(db.Integer,db.ForeignKey('usuario.idusuario'))

    def __init__(self,ruc,nombre_anfitrion,numero_contacto,departamento,idusuario):
        self.ruc=ruc,
        self.nombre_anfitrion=nombre_anfitrion,
        self.numero_contacto=numero_contacto,
        self.departamento=departamento
        self.idusuario=idusuario

class NegocioTuristicoSchema(ma.Schema):
    class Meta:
        fields =('idnegocio_turistico','ruc','nombre_anfitrion','numero_contacto','departamento')

negocioturistico_schema = NegocioTuristicoSchema()
negociosturisticos_schema = NegocioTuristicoSchema(many=True)

@app.route('/negocioturist',methods=['POST'])
def create_negocioturistico():
    
    print(request.json)
    ruc= request.json['ruc'],
    nombre_anfitrion=request.json['nombre_anfitrion']
    numero_contacto =request.json['numero_contacto']
    departamento=request.json['departamento']
    idusuario=request.json['idusuario']
    nuevo_negocio =NegocioTuristico(ruc,nombre_anfitrion,numero_contacto,departamento,idusuario)
    
    db.session.add(nuevo_negocio)
    db.session.commit()

    return negocioturistico_schema.jsonify(nuevo_negocio)

@app.route('/listarnegociosturist',methods=['GET'])
def get_negociosturis():
    listar_negocios= NegocioTuristico.query.all()
    result = negociosturisticos_schema.dump(listar_negocios)

    return jsonify(result)

@app.route('/buscarnegocioturist/<idnegocio_turistico>',methods=['GET'])
def buscar_negocioturist(idnegocio_turistico):
    negocio_encontrado = NegocioTuristico.query.get(idnegocio_turistico)
    return negocioturistico_schema.jsonify(negocio_encontrado)

@app.route('/negocioturist/<idnegocio_turistico>',methods=['PUT'])
def actualizar_negocioturist(idnegocio_turistico):
    negocio_encontrado = NegocioTuristico.query.get(idnegocio_turistico)
    
    ruc= request.json['ruc'],
    nombre_anfitrion=request.json['nombre_anfitrion']
    numero_contacto =request.json['numero_contacto']
    departamento=request.json['departamento']

    negocio_encontrado.ruc= ruc
    negocio_encontrado.nombre_anfitrion= nombre_anfitrion
    negocio_encontrado.numero_contacto = numero_contacto
    negocio_encontrado.departamento= departamento

    db.session.commit()
    return negocioturistico_schema.jsonify(negocio_encontrado)

@app.route('/eliminarnegocio/<idnegocio_turistico>',methods=['DELETE'])
def eliminar_negocioturis(idnegocio_turistico):
    negocio_encontrado = NegocioTuristico.query.get(idnegocio_turistico)
    db.session.delete(negocio_encontrado)
    db.session.commit()

    return negocioturistico_schema.jsonify(negocio_encontrado)


#MODELO de REGION
class Region(db.Model):
    idregion =db.Column(db.Integer,primary_key=True)
    nombre_region=db.Column(db.String)


#MODELO DE USUARIO
class Cliente(db.Model):
    idcliente = db.Column(db.Integer,primary_key=True)
    nombre_completo =db.Column(db.String(100),unique=True)
    dni =db.Column(db.String(45))
    idusuario=db.Column(db.Integer,db.ForeignKey('usuario.idusuario'))
    def __init__(self,nombre_completo,dni,idusuario):
        self.nombre_completo=nombre_completo,
        self.dni=dni
        self.idusuario=idusuario

class ClienteSchema(ma.Schema):
    class Meta:
        fields =('idcliente','nombre_completo','dni')

usuario_schema = ClienteSchema()
usuarios_schema = ClienteSchema(many=True)

@app.route('/usuario',methods=['POST'])
def create_usuario():

    print(request.json)
    nombre_completo= request.json['nombre_completo']

    dni=request.json['dni']
    idusuario=request.json['idusuario']
    nuevo_usuario =Cliente(nombre_completo,dni,idusuario)
    db.session.add(nuevo_usuario)
    db.session.commit()

    return usuario_schema.jsonify(nuevo_usuario)
    #return request.json

#MODELO DE EXCURSION
class Excursion(db.Model):
    idexcursion=db.Column(db.Integer,primary_key=True)
    #regiones=db.relationship('Region',backref='region')
    idregion=db.Column(db.Integer,db.ForeignKey('region.idregion'))
    foto_portada=db.Column(db.String(255))
    nombre_excursion=db.Column(db.String(255))
    descripcion= db.Column(db.TEXT(20000000))
    duracion=db.Column(db.String(25))
    precio=db.Column(db.Numeric)
    departamento = db.Column(db.String(45))
    medio_pago=db.Column(db.String(45))
    fecha_inicio=db.Column(db.DATE)
    fecha_fin=db.Column(db.DATE)
    aforo= db.Column(db.Integer)
    incluye=db.Column(db.String(255))
    no_incluye=db.Column(db.String(255))
    idnegocio_turistico=db.Column(db.Integer,db.ForeignKey('negocio_turistico.idnegocio_turistico'))

# #MODELO DE SOLICITUD DE RESERVA


# #MODELO DE ITINERARIO



if __name__ == '__main__':
    app.run(debug=True)


@app.route('/',methods =['GET'])
def index():
    return jsonify({"message":"bienvenido a mi api"})