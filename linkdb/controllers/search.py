import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from linkdb.lib.base import BaseController, render
from linkdb.model import *
from linkdb.model.meta import Session

from webhelpers.paginate import Page

log = logging.getLogger(__name__)

class SearchController(BaseController):

    def search(self):
        if not request.GET.has_key('query'):
            c.flash = 'Please enter a search query in the box above'
            return render('/search.mako')

        query = request.GET['query']
        links = Session.query(Link).filter("MATCH (`title`, `description`) AGAINST(:query)").params(query=query)

        if request.GET.has_key('page'):
            page = request.GET['page']
        else:
            page = 1

        c.pager = Page(links, page=page, items_per_page=10, query=query)
        c.query = query

        return render('/search.mako')
