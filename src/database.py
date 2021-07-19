from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

engine = create_engine('mysql+pymysql://root:030115lol@localhost/rutusbd')
#we have to update the name of the data base"

Base = declarative_base()

Session = sessionmaker(bind=engine)