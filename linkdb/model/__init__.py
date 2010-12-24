'''The application's model objects'''
from sqlalchemy import *
from sqlalchemy.orm import *

from linkdb.model import meta, forms
from linkdb.model.auth import MyUsersFromDatabase

def init_model(engine):
    '''Call me before using any of the tables or classes in the model'''
    meta.Session.configure(bind=engine)
    meta.engine = engine

class User(object):
    def __init__(self, username, password=None, email=None, group_uid=None):
        self.username   = username
        self.password   = password
        self.group_uid  = group_uid
        self.email      = email
    def __repr__(self):
        return 'User(%(username)s)' % self.__dict__

class Group(object):
    def __init__(self, name=None):
        self.name = name
    def __repr__(self):
        return 'Group(%(name)s)' % self.__dict__
        
class Role(object):
    def __init__(self, name=None):
        self.name = name
    def __repr__(self):
        return 'Role(%(name)s)' % self.__dict__
        
# Tables
groups_table = Table(
    'groups',
    meta.metadata,
    Column('uid',        Integer,        primary_key=True),
    Column('name',      String(255),    unique=True,    nullable=False),
)
roles_table = Table(
    'roles',
    meta.metadata,
    Column('uid',        Integer,        primary_key=True),
    Column('name',      String(255),    unique=True,    nullable=False),
)
users_table = Table(
    'users',
    meta.metadata,
    Column('uid',        Integer,        primary_key=True),
    Column('username',  String(255),    unique=True,    nullable=False),
    Column('password',  String(255),     nullable=False),
    Column('group_uid',  Integer,        ForeignKey('groups.uid')),
    Column('email',     String(255),    unique=True, nullable=False),
    Column('joined',    DateTime,        default=func.now()),
)
users_roles_table = Table(                # many:many relation table
    'users_roles',
    meta.metadata,
    Column('user_uid',   Integer,        ForeignKey('users.uid')),
    Column('role_uid',   Integer,        ForeignKey('roles.uid')),
)
# Uses the mapper as part of the Session
mapper(
    Group,
    groups_table,
    properties={
        'users': relation(User)
    }
)
mapper(
    User,
    users_table,
    properties={
        'roles': relation(Role, lazy=True, secondary=users_roles_table),
        'group': relation(Group),
    }
)
mapper(
    Role,
    roles_table,
    properties={
        'users': relation(User, lazy=True, secondary=users_roles_table)
    }
)

class Link(object):
    def __repr__(self):
        return 'Link(%(url)s)' % self.__dict__

    @staticmethod
    def search(query):
        pass

class Category(object):
    def __init__(self, name):
        self.name = name

    def count_links(self):
        return meta.Session.query(Link).filter_by(category_id=self.category_id).count()

    def __repr__(self):
        return 'Category(%(name)s)' % self.__dict__

class Letter(object):
    def __init__(self, letter, link_id):
        self.letter = letter
        self.link_id = link_id

    def count_links(self):
        return meta.Session.query(Letter).filter_by(letter=self.letter).count()

    @staticmethod
    def get_links(letter):
        return meta.Session.query(Letter).filter_by(letter=letter).add_entity(Link).join('links').from_self(Link)

    def __repr__(self):
        return 'Letter(%(letter)s)' % self.__dict__

class SearchTerm(object):
    def __repr__(self):
        return 'SearchTerm(%(term)s)' % self.__dict__

link_table = Table('links', meta.metadata,
    Column('link_id', Integer, primary_key=True),
    Column('title', Unicode(255), nullable=False),
    Column('url', String(255), unique=True, nullable=False),
    Column('description', UnicodeText()),
    Column('category_id', Integer, ForeignKey('categories.category_id'), nullable=False, default=1),
    Column('user_id', Integer, ForeignKey('users.uid')),
    Column('date_added', DateTime, default=func.now()),
    Column('date_updated', DateTime, onupdate=func.current_timestamp()),
    Column('visit_count', Integer, nullable=False, default=0),
    )
mapper(Link, link_table, properties={
    'submitted_by': relation(User, lazy=True),
    'category': relation(Category),
    })

category_table = Table('categories', meta.metadata,
    Column('category_id', Integer, primary_key=True),
    Column('name', Unicode(255), nullable=False),
    )
mapper(Category, category_table, properties={
    'links': relation(Link, backref='categories', lazy=True),
#    'link_count': column_property(
#        select([func.count(link_table.c.link_id)]).label('link_count')),
    })

letter_table = Table('letters', meta.metadata,
    Column('letter', String(1)),
    Column('link_id', Integer, ForeignKey('links.link_id'), primary_key=True),
    )
mapper(Letter, letter_table, properties={
    'links': relation(Link, uselist=True, lazy=True),
    })

searchterm_table = Table('search_terms', meta.metadata,
    Column('term', Unicode(50), primary_key=True),
    Column('count', Integer, nullable=False),
    )
mapper(SearchTerm, searchterm_table)

## Non-reflected tables may be defined and mapped at module level
#foo_table = Table('Foo', meta.metadata,
#    Column('id', Integer, primary_key=True),
#    Column('bar', String(255), nullable=False),
#    )
#
#class Foo(object):
#    pass
#
#mapper(Foo, foo_table)
