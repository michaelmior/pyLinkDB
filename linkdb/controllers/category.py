import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from linkdb.lib.base import BaseController, render
from linkdb.model.meta import Session
from linkdb.model import *

from authkit.permissions import HasAuthKitGroup
from authkit.authorize.pylons_adaptors import authorize
from webhelpers.paginate import Page

log = logging.getLogger(__name__)

class CategoryController(BaseController):

    @authorize(HasAuthKitGroup(['admin']))
    def edit(self, id=None):
        if id:
            c.category = Session.query(Category).get(id)
        else:
            c.category = None

        return render('/category/edit.mako')

    @authorize(HasAuthKitGroup(['admin']))
    def save(self, id=None):
        if id:
            # Find the existing category
            category = Session.query(Category).get(id)
            if category is None:
                abort(404)

            category.name = request.POST.get('name')
        else:
            # Create a new category
            category = Category(request.POST.get('name'))

        # Save the new category
        Session.save_or_update(category)
        Session.commit()

        return redirect_to(controller='browse', action='categories')

    @authorize(HasAuthKitGroup(['admin']))
    def delete(self, id):
        category = Session.query(Category).get(id)
        
        if category is None:
            abort(404)

        Session.delete(category)
        Session.commit()

        redirect_to(controller='browse', action='categories', _code=303)
