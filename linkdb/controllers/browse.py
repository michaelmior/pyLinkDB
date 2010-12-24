import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from linkdb.lib.base import BaseController, render
import linkdb.lib.helpers as h
from linkdb.model import *
from linkdb.model.meta import Session

from webhelpers.paginate import Page

log = logging.getLogger(__name__)

class BrowseController(BaseController):

    def index(self):
        redirect_to(controller='browse', action='categories')

    def letters(self, id=None, page=1):
        # Dipslay the letter listing page if no letter specified
        letter = id
        if not letter:
            c.letters = Session.query(Letter).order_by(Letter.letter).group_by(Letter.letter).all()
            return render('/browse/letters.mako')

        # Produce an error if the letter doesn't exist
        if len(letter) > 1 or not letter.isupper() or Session.query(Letter).filter_by(letter=letter).count() == 0:
            abort(404)

        # Get all links with the letter and display the listing
        c.letter = letter.upper()

        links = Letter.get_links(letter)
        c.pager = Page(links, page=page, items_per_page=10)
        return render('/browse/letter.mako')

    def categories(self, id=None, name=None, page=1):
        # Display the category listing page if no id is specified
        if not id:
            c.categories = Session.query(Category).all()
            return render('/browse/categories.mako')

        # Get the category name and redirect if necessary
        if not name:
            category = id and Session.query(Category).get(id)
            if category:
                redirect_to(controller='browse', action='categories', id=id, name=h.name_to_url(category.name))
            else:
                abort(404)

        # Get all links in the category and display the listing
        c.category = Session.query(Category).get(id)
        links = Session.query(Link).filter_by(category_id=id)
        c.pager = Page(links, page=page, items_per_page=10)

        return render('/browse/category.mako')

    def new(self, page=1):
        links = Session.query(Link).order_by(desc(Link.date_added))
        c.pager = Page(links, page=page, items_per_page=10)

        return render('/browse/new.mako')

    def popular(self, page=1):
        links = Session.query(Link).order_by(desc(Link.visit_count))
        c.pager = Page(links, page=page, items_per_page=10)

        return render('/browse/popular.mako')
