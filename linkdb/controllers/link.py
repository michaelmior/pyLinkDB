import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect, redirect_to

from linkdb.lib.base import BaseController, render, validate
from linkdb.model import *
from linkdb.model.meta import Session

from authkit.permissions import HasAuthKitGroup
from authkit.authorize.pylons_adaptors import authorize

log = logging.getLogger(__name__)

class LinkController(BaseController):

    def view(self, id):
        c.link = Session.query(Link).get(id)

        return render('/link/view.mako')

    @authorize(HasAuthKitGroup(['admin']))
    def edit(self, id=None):
        """
        Display the add/edit form, retrieving existing link data
        if necessary.
        """
        if id:
            c.link = Session.query(Link).get(id)
        else:
            c.link = None

        c.categories = Session.query(Category).all()

        return render('/link/edit.mako')

    @authorize(HasAuthKitGroup(['admin']))
    @validate(schema=forms.LinkForm(), form='edit')
    def save(self):
        id = request.POST.get('id')
        if id:
            link = Session.query(Link).get(id)
        else:
            link = Link()

        # Apply the values to the link object
        link.title       = self.form_result['title']
        link.url         = self.form_result['url']
        link.description = self.form_result['description']
        link.category_id = self.form_result['category_id']

        Session.save_or_update(link)
        Session.commit()

    @authorize(HasAuthKitGroup(['admin']))
    def delete(self):
        """
        Delete a link from the database (make sure the user is an admin).
        """
        id = request.POST.get('id', None)
        if id:
            link = Session.query(Link).get(id)
            Session.delete(link)
            Session.commit()

        return ''

    def out(self, id):
        """
        Send the visitor to the website pointed to by the link.
        Also update the link's visited counter.
        """
        link = Session.query(Link).filter_by(link_id=id).first()
        link.visit_count += 1
        #Session.update(link)

        redirect(link.url, code=303)
