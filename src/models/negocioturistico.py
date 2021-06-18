from ..database import Base
from sqlalchemy import Column,Integer,String,Float

class NegocioTuristico(Base):
    __tablename__ ='negocioturistico'

    idnegocio_turistico = Column(Integer,primary_key=True)
    ruc =Column(String,unique=True)
    nombre_anfitrion=Column(String)
    numero_contacto =Column(String)
    departamento =Column(String)

    def __init__(self,ruc,nombre_anfitrion,numero_contacto,departamento):
        self.ruc=ruc,
        self.nombre_anfitrion=nombre_anfitrion,
        self.numero_contacto=numero_contacto,
        self.departamento=departamento

# class NegocioTuristicoSchema(ma.Schema):
#     class Meta:
#         fields =('idnegocio_turistico','ruc','nombre_anfitrion','numero_contacto','departamento')

# negocioturistico_schema = NegocioTuristicoSchema()
# negociosturisticos_schema = NegocioTuristicoSchema(many=True)