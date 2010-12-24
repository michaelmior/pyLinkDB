import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from linkdb.lib.base import BaseController, render

log = logging.getLogger(__name__)

class UsersController(BaseController):

    def login(self):
        if not request.environ.get('REMOTE_USER'):
            abort(401)
        else:
            redirect_to(controller='browse', action='index', _code=303)

    def logout(self):
        redirect_to(controller='browse', action='index', _code=307)
