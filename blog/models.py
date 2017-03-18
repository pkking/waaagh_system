from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql import func
from flask_restful import abort
import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class CRUDMixin(object):
    def __repr__(self):
        return "<{}>".format(self.__class__.__name__)

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    def save(self):
        """Saves the object to the database."""
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        """Delete the object from the database."""
        db.session.delete(self)
        db.session.commit()
        return self

class TableMixin(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

class FindMixin(object):
    @classmethod
    def get_all(cls):
        res = cls.query.all()
        if not res:
            abort(404, message="not any {} exist".format(cls.__name__))
        else:
            return res

    @classmethod
    def find_by_id(cls, id):
        res = cls.query.get(id)
        if not res:
            abort(404, message="{} id {} doesn't exist".format(cls.__name__, id))
        else:
            return res

    @classmethod
    def find_by_name(cls, name):
        if not hasattr(cls, 'name'):
            return []
        res = cls.query.filter_by(name=name).all()
        if not res:
            abort(404, message="{} name {} doesn't exist".format(cls.__name__, name))
        else:
            return res

    @classmethod
    def created_during(cls, begin, end):
        cls.time_during(cls, 'created', begin, end)

    @classmethod
    def login_during(cls, begin, end):
        cls.time_during(cls, 'last_login', begin, end)

    @classmethod
    def time_during(cls, attr, begin, end):
        if not hasattr(cls, attr):
            return []
        b = begin if begin else datetime.datetime.min
        e = end if end else datetime.datetime.max
        res = cls.query.filter(cls.created <= e, cls.created >= b).all()
        if not res:
            abort(404, message="no {} created during [{} - {}]".format(cls.__name__, begin, end))
        else:
            return res
    
    @classmethod
    def find_by_email(cls, email):
        if not hasattr(cls, 'time'):
            return []
        res = cls.query.filter_by(email=email).all()
        if not res:
            abort(404, message="{} email {} doesn't exist".format(cls.__name__, email))
        else:
            return res

class Post(db.Model, TableMixin, CRUDMixin, FindMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    body = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    modified = db.Column(db.DateTime(timezone=True), server_default=func.now(), 
            onupdate=datetime.datetime.utcnow, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('persion.id'))
     
            
class Persion(db.Model, TableMixin, CRUDMixin, FindMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50))
    created = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    last_login = db.Column(db.DateTime(timezone=True), server_default=func.now(), 
            onupdate=datetime.datetime.utcnow, nullable=False)
    posts = db.relationship('Post', order_by="Post.id", backref=db.backref('author'))
    
association_table = db.Table('association', db.metadata,
                          db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
                          db.Column('post_id', db.Integer, db.ForeignKey('post.id'))
                          )

class Tag(db.Model, TableMixin, CRUDMixin, FindMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    created = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    posts = db.relationship('Post', secondary=association_table, order_by="Post.id", 
            backref=db.backref('tags', lazy='dynamic'))