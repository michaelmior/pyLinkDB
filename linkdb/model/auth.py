# SQLAlchemy 0.5 Driver for AuthKit
# Based on the SQLAlchemy 0.4.4 driver but using session.add() instead of 
# session.save()

# This file assumes the following in the model used in Pylons 0.9.7

from sqlalchemy import *
from paste.util.import_string import eval_import
from authkit.users import *
from authkit.users.sqlalchemy_driver import UsersFromDatabase

from sqlalchemy.orm import *

from linkdb.lib.base import  render

class MyUsersFromDatabase(UsersFromDatabase):
    """
    Database Version
    """
    def __init__(self, model, encrypt=None):
        if encrypt is None:
            def encrypt(password):
                return password
        self.encrypt = encrypt
        if isinstance(model, (str, unicode)):
            model = eval_import(model)
        if hasattr(model, 'authkit_initialized'):
            raise AuthKitError(
                'The AuthKit database model has already been setup'
            )
        else:
            model.authkit_initialized = True

        # Update the model
        self.model = model
        self.meta = self.model.meta    

    def update_model(self, model):
        return model

def make_template():
    return render('/users/login.mako').replace('FORM_ACTION', '%s')
