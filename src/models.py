import os
import sys
from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

seguidores = Table('seguidores', 
    Base.metadata,
    Column('id_user_seg', Integer, ForeignKey('usuario.id'), primary_key=True),
    Column('id_user_followers', Integer, ForeignKey('usuario.id'), primary_key=True)
)

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    userName = Column(String(250), nullable=False)
    eMail = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    #Seguidores
    following = relationship('followers', secondary=seguidores)


class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comentario = Column(String(250), nullable=False)
    id_user = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    id_post = Column(Integer, ForeignKey('post.id'), nullable=False)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    tipo = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    id_post = Column(Integer, ForeignKey('post.id'), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    # Comentarios
    comments = relationship("Comments", backref="comments")
    #Media
    media = relationship("Media", backref="media")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')