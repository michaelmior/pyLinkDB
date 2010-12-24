"""The base Controller API

Provides the BaseController class for subclassing.
"""
from pylons import tmpl_context as c
from pylons.controllers import WSGIController
from pylons.templating import render_mako as render
from pylons.decorators import *

from linkdb.model import meta

from authkit.permissions import HasAuthKitGroup
from authkit.authorize.pylons_adaptors import authorized

def get_order(order):
    #if order == 'popular':
    #    return Link.visit_count
    #elif order == 'latest':
    #    return Link.date_updated
    #else:
    #    return Link.title
    pass

class BaseController(WSGIController):

    def __before__(self, action, **params):
        c.admin = authorized(HasAuthKitGroup(['admin']))

    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # WSGIController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']
        try:
            return WSGIController.__call__(self, environ, start_response)
        finally:
            meta.Session.remove()
