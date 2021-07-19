from flask import Flask,jsonify,request
from decimal import Decimal
from datetime import datetime
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Response
import json

#from .controllers.negocioturistico_controller import NegocioTurisController

app = Flask(__name__)
api= Api(app)
db = SQLAlchemy(app)
ma= Marshmallow(app)

app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:030115lol@localhost/rutusbd'


#api.add_resource(NegocioTurisController,'/negocioturistico')
#MODELO TIPO DE USUARIO DE USUARIO

class TipoUsuario(db.Model):
    idtipo_usuario = db.Column(db.Integer,primary_key=True)
    descripcion = db.Column(db.String(45))

class TipoUsuarioSchema(ma.Schema):
    class Meta:
        fields = ('idtipo_usuario','descripcion')

#MODELO USUARIO
class Usuario(db.Model):
    idusuario = db.Column(db.Integer,primary_key=True)
    correo=db.Column(db.String(45),unique=True)
    contrasenia=db.Column(db.String(45))
    idtipo_usuario=db.Column(db.Integer,db.ForeignKey('tipo_usuario.idtipo_usuario'))

    def __init__(self,correo,contrasenia,idtipo_usuario):
        self.correo = correo
        self.contrasenia = contrasenia
        self.idtipo_usuario=idtipo_usuario

class UsuarioSchema(ma.Schema):
    class Meta:
        fields =('idusuario','correo','contrasenia','idtipo_usuario')

usuario_schema = UsuarioSchema()
usuarios_schema= UsuarioSchema(many= True)

@app.route('/usuario',methods=['POST'])
def create_user():
    print(request.json)
    correo=request.json['correo'],
    contrasenia=request.json['contrasenia']
    idtipo_usuario=request.json['idtipo_usuario']
    nuevo_usuario = Usuario(correo=correo,contrasenia=contrasenia,idtipo_usuario=idtipo_usuario)
    
    db.session.add(nuevo_usuario)
    db.session.commit()

    message={
        "status":200,
        "message":"Usuario creado correctamente",
        "result":usuario_schema.dump(nuevo_usuario)
    }

    return jsonify(message)

    #return usuario_schema.jsonify(nuevo_usuario)

@app.route('/usuario/<idusuario>',methods=['PUT'])
def actualizar_user(idusuario):
    print(request.json)
    usuario_encontrado = Usuario.query.get(idusuario)

    correo=request.json['correo'],
    contrasenia=request.json['contrasenia']
    usuario_encontrado.correo=correo
    usuario_encontrado.contrasenia=contrasenia

    db.session.commit()

    message={
        "status":200,
        "message":"Usuario actualizado correctamente",
        "result":usuario_schema.dump(usuario_encontrado)
    }

    return jsonify(message)

    #return usuario_schema.jsonify(usuario_encontrado)

@app.route('/listarusuarios',methods=['GET'])
def get_usuarios():
    listar_usuarios= Usuario.query.all()
   
    #result = usuarios_schema.dump(listar_usuarios)
    
    message={
        "status":200,
        "message":"OK",
        "result":usuarios_schema.dump(listar_usuarios)
    }

    return jsonify(message)

#MODELO DE NEGOCIO TURISTICO
class NegocioTuristico(db.Model):
    idnegocio_turistico = db.Column(db.Integer,primary_key=True)
    ruc =db.Column(db.String(45),unique=True)
    nombre_anfitrion=db.Column(db.String(45))
    numero_contacto =db.Column(db.String(45))
    departamento =db.Column(db.String(45))
    idusuario=db.Column(db.Integer,db.ForeignKey('usuario.idusuario',ondelete='CASCADE'))
    #idusuario=db.relationship('Usuario',backref='idusuario')

    def __init__(self,ruc,nombre_anfitrion,numero_contacto,departamento,idusuario):
        self.ruc=ruc,
        self.nombre_anfitrion=nombre_anfitrion,
        self.numero_contacto=numero_contacto,
        self.departamento=departamento
        self.idusuario=idusuario

class NegocioTuristicoSchema(ma.Schema):
    class Meta:
        fields =('idnegocio_turistico','ruc','nombre_anfitrion','numero_contacto','departamento','idusuario')

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

    message={
        "status":200,
        "message":"Negocio turístico creado correctamente",
        "result":negocioturistico_schema.dump(nuevo_negocio)
    }

    return jsonify(message)

    #return negocioturistico_schema.jsonify(nuevo_negocio)

@app.route('/listarnegociosturist',methods=['GET'])
def get_negociosturis():
    listar_negocios= NegocioTuristico.query.all()

   # result = negociosturisticos_schema.dump(listar_negocios)

    message={
        "status":200,
        "message":"OK",
        "result":negociosturisticos_schema.dump(listar_negocios)
    }

    return jsonify(message)
    
    #return jsonify(result)

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

    message={
        "status":200,
        "message":"Negocio turísitico actualizado correctamente",
        "result":negocioturistico_schema.dump(negocio_encontrado)
    }

    return jsonify(message)

    #return negocioturistico_schema.jsonify(negocio_encontrado)

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


#MODELO DE CLIENTE
class Cliente(db.Model):
    idcliente = db.Column(db.Integer,primary_key=True)
    nombre_completo =db.Column(db.String(100),unique=True)
    dni =db.Column(db.String(45))
    idusuario=db.Column(db.Integer,db.ForeignKey('usuario.idusuario',ondelete='CASCADE'))
    usuario=db.relationship("Usuario",backref="cliente",single_parent=True)

    def __init__(self,nombre_completo,dni,idusuario):
        self.nombre_completo=nombre_completo,
        self.dni=dni
        self.idusuario=idusuario

class ClienteSchema(ma.Schema):
    class Meta:
        fields =('idcliente','nombre_completo','dni','idusuario','idusuario.idtipo_usuario')

cliente_schema = ClienteSchema()
clientes_schema = ClienteSchema(many=True)

@app.route('/cliente',methods=['POST'])
def create_usuario():

    print(request.json)
    nombre_completo= request.json['nombre_completo']
    dni=request.json['dni']
    idusuario=request.json['idusuario']
    nuevo_cliente =Cliente(nombre_completo,dni,idusuario)

    db.session.add(nuevo_cliente)
    db.session.commit()

    message={
        "status":200,
        "message":"OK",
        "result":cliente_schema.dump(nuevo_cliente)
    }
    print(message)

    
    #return cliente_schema.jsonify(nuevo_cliente)
    return jsonify(message)

@app.route('/listarclientes',methods=['GET'])
def get_clientes():
    listar_clientes= Cliente.query.all()
    print(listar_clientes)
    
    message={
        "status":200,
        "message":"OK",
        "result":clientes_schema.dump(listar_clientes)
    }

    
    
    print(message)
    # resultmessa = clientes_schema.dumps(message)
    # resp = jsonify(resultmessa)
    # resp.status = 200

   # return jsonify(clientes_schema.dumps(listar_clientes))
    result = clientes_schema.dump(message)

    print(result)

    return jsonify(message)

@app.route('/eliminarcliente/<idcliente>',methods=['DELETE'])
def eliminar_cliente(idcliente):
    cliente_encontrado = Cliente.query.get(idcliente)
    db.session.delete(cliente_encontrado)
    db.session.commit()

    return cliente_schema.jsonify(cliente_encontrado)

#MODELO DE EXCURSION
class Excursion(db.Model):
    idexcursion=db.Column(db.Integer,primary_key=True)
    #regiones=db.relationship('Region',backref='region')
    idregion=db.Column(db.Integer,db.ForeignKey('region.idregion'))
    foto_portada=db.Column(db.String(255))
    nombre_excursion=db.Column(db.String(255))
    descripcion= db.Column(db.TEXT(20000000))
    duracion=db.Column(db.String(25))
    precio_persona=db.Column(db.Numeric)
    departamento = db.Column(db.String(45))
    medio_pago=db.Column(db.String(45))
    fecha_inicio=db.Column(db.DATE)
    fecha_fin=db.Column(db.DATE)
    aforo= db.Column(db.Integer)
    incluye=db.Column(db.String(255))
    no_incluye=db.Column(db.String(255))
    idnegocio_turistico=db.Column(db.Integer,db.ForeignKey('negocio_turistico.idnegocio_turistico'))

    def __init__(self,idregion,foto_portada,nombre_excursion,descripcion,duracion,precio_persona,departamento,medio_pago,fecha_inicio,fecha_fin,aforo,incluye,no_incluye,idnegocio_turistico):
        self.idregion=idregion,
        self.foto_portada=foto_portada
        self.nombre_excursion=nombre_excursion
        self.descripcion=descripcion
        self.duracion=duracion
        self.precio_persona=precio_persona
        self.departamento=departamento
        self.medio_pago=medio_pago
        self.fecha_inicio=fecha_inicio
        self.fecha_fin=fecha_fin
        self.aforo=aforo
        self.incluye=incluye
        self.no_incluye=no_incluye
        self.idnegocio_turistico=idnegocio_turistico

class ExcursionSchema(ma.Schema):
    class Meta:
        fields =('idexcursion','idregion','foto_portada','nombre_excursion','descripcion','duracion','precio_persona','departamento','medio_pago','fecha_inicio','fecha_fin','aforo','inclye','no_incluye','idnegocio_turistico')

excursion_schema = ExcursionSchema()
excursiones_schema = ExcursionSchema(many=True)

@app.route('/excursion',methods=['POST'])
def create_excursion():
    
    print(request.json)
    idregion= request.json['idregion'],
    foto_portada=request.json['foto_portada']
    nombre_excursion =request.json['nombre_excursion']
    descripcion=request.json['descripcion']
    duracion=request.json['duracion']
    precio_persona=request.json['precio_persona']
    departamento=request.json['departamento']
    medio_pago=request.json['medio_pago']
    fecha_inicio=request.json['fecha_inicio']
    fecha_fin=request.json['fecha_fin']
    aforo=request.json['aforo']
    incluye=request.json['incluye']
    no_incluye=request.json['no_incluye']
    idnegocio_turistico=request.json['idnegocio_turistico']

    nueva_excursion =Excursion(idregion,foto_portada,nombre_excursion,descripcion,duracion,precio_persona,departamento,medio_pago,fecha_inicio,fecha_fin,aforo,incluye,no_incluye,idnegocio_turistico)
    
    db.session.add(nueva_excursion)
    db.session.commit()

    message={
        "status":200,
        "message":"Excursión creada correctamente",
        "result":excursion_schema.dump(nueva_excursion)
    }
    print(message)

    return jsonify(message)
    #return "probando"

    #return negocioturistico_schema.jsonify(nuevo_negocio)

@app.route('/listarexcursiones',methods=['GET'])
def get_excursiones():
    listar_excursiones= Excursion.query.all()

   # result = negociosturisticos_schema.dump(listar_negocios)

    message={
        "status":200,
        "message":"OK",
        "result":excursiones_schema.dump(listar_excursiones)
    }

    return jsonify(message)
    
    #return jsonify(result)


@app.route('/buscarexcursion/<idexcursion>',methods=['GET'])
def buscar_excursion(idexcursion):
    excursion_encontrada = Excursion.query.get(idexcursion)
    return excursion_schema.jsonify(excursion_encontrada)

# #MODELO DE SOLICITUD DE RESERVA
class MedioPago(db.Model):
    idmedio_pago = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(45))

    def __init__(self,idmedio_pago,descripcion):
        self.idmedio_pago=idmedio_pago,
        self.descripcion=descripcion

class MedioPagoSchema(ma.Schema):
    class Meta:
        fields =('idmedio_pago','descripcion')

megiopago_schema = MedioPagoSchema()
megiopagos_schema = MedioPagoSchema(many=True)

class SolicitudReserva(db.Model):
    idsolicitud_reserva=db.Column(db.Integer,primary_key=True)
    #regiones=db.relationship('Region',backref='region')
    idexcursion=db.Column(db.Integer,db.ForeignKey('excursion.idexcursion'))
    precio_total= db.Column(db.Numeric)
    fecha_registro=db.Column(db.DATE)
    estado_solicitud= db.Column(db.Integer)
    cantidad_acompaniantes=db.Column(db.String(45))
    idcliente=db.Column(db.Integer,db.ForeignKey('cliente.idcliente'))
    idmedio_pago=db.Column(db.Integer,db.ForeignKey('medio_pago.idmedio_pago'))
    nombre_excursion=db.Column(db.String(100))
    nombre_cliente = db.Column(db.String(100))

    def __init__(self,idexcursion,nombre_excursion,precio_total,fecha_registro,estado_solicitud,cantidad_acompaniantes,idmedio_pago,idcliente,nombre_cliente):
        self.idexcursion = idexcursion
        self.nombre_excursion = nombre_excursion
        self.precio_total = precio_total
        self.fecha_registro = fecha_registro
        self.estado_solicitud = estado_solicitud
        self.cantidad_acompaniantes = cantidad_acompaniantes
        self.idmedio_pago = idmedio_pago
        self.idcliente = idcliente
        self.nombre_cliente = nombre_cliente

class SolicitudReservaSchema(ma.Schema):
    class Meta:
        fields =('idsolicitud_reserva','idexcursion','nombre_excursion',
        'precio_total','fecha_registro','estado_solicitud','cantidad_acompaniantes',
        'idmedio_pago','idcliente','nombre_cliente')

solicitudreserva_schema = SolicitudReservaSchema()
solicitudreservas_schema = SolicitudReservaSchema(many=True)

@app.route('/solicitudreserva',methods=['POST'])
def create_solicitud():

    print(request.json)
    idexcursion= request.json['idexcursion']
    nombre_excursion= request.json['nombre_excursion']
    precio_total=request.json['precio_total']
    fecha_registro= request.json['fecha_registro']
    estado_solicitud=request.json['estado_solicitud']
    cantidad_acompaniantes=request.json['cantidad_acompaniantes']
    idmedio_pago=request.json['idmedio_pago']
    idcliente =request.json['idcliente']
    nombre_cliente=request.json['nombre_cliente']
    nueva_solicitud = SolicitudReserva(idexcursion,nombre_excursion,precio_total,fecha_registro,estado_solicitud,cantidad_acompaniantes,idmedio_pago,idcliente,nombre_cliente)

    db.session.add(nueva_solicitud)
    db.session.commit()

    message={
        "status":200,
        "message":"OK",
        "result":solicitudreserva_schema.dump(nueva_solicitud)
    }
    print(message)
    #raise KeyError(message)
    
    #return cliente_schema.jsonify(nuevo_cliente)
    return jsonify(message)

@app.route('/listarsolireser',methods=['GET'])
def get_solicitudesreserva():
    listar_solicitudes= SolicitudReserva.query.all()

   # result = negociosturisticos_schema.dump(listar_negocios)

    message={
        "status":200,
        "message":"OK",
        "result":solicitudreservas_schema.dump(listar_solicitudes)
    }

    return jsonify(message)
    
    #return jsonify(result)

@app.route('/detallesolici/<idsolicitud_reserva>',methods=['GET'])
def detalle_solicitud(idsolicitud_reserva):
    solicitud_encontrada = SolicitudReserva.query.get(idsolicitud_reserva)
    return solicitudreserva_schema.jsonify(solicitud_encontrada)

#PAGAR SOLICITUD DE RESERVA CONFIRMADA

class Reserva(db.Model):
    idreserva = db.Column(db.Integer,primary_key=True)
    idsolicitud_reserva = db.Column(db.Integer,db.ForeignKey('solicitud_reserva.idsolicitud_reserva'))
    fecha_registro=db.Column(db.DATE)
    nombre_cliente = db.Column(db.String(100))

    def __init__(self,idsolicitud_reserva,fecha_registro,nombre_cliente):
        self.idsolicitud_reserva = idsolicitud_reserva
        self.fecha_registro = fecha_registro
        self.nombre_cliente = nombre_cliente

class ReservaSchema(ma.Schema):
    class Meta:
        fields =('idreserva','idsolicitud_reserva','fecha_registro','nombre_cliente')

reserva_schema = ReservaSchema()
reservas_schema = ReservaSchema(many=True)

@app.route('/registrarreserva',methods=['POST'])
def create_reserva():

    print(request.json)
    
    idsolicitud_reserva = request.json['idsolicitud_reserva']
    fecha_registro = request.json['fecha_registro']
    nombre_cliente=request.json['nombre_cliente']
    
    nueva_reserva = Reserva(idsolicitud_reserva,fecha_registro,nombre_cliente)
    #print(nueva_reserva)
    db.session.add(nueva_reserva)
    db.session.commit()

    message={
        "status":200,
        "message":"OK",
        "result":reserva_schema.dump(nueva_reserva)
    }
    print(message)
    #raise KeyError(message)
    
    #return cliente_schema.jsonify(nuevo_cliente)
    return jsonify(message)
    
# #MODELO DE ITINERARIO



if __name__ == '__main__':
    app.run(debug=True)


@app.route('/',methods =['GET'])
def index():
    return jsonify({"message":"bienvenido a mi api"})