from linkdb.model import *
from linkdb.model.meta import Session

def total_hits():
    hits = Session.query(func.sum(Link.visit_count)).one()[0]
    if hits:
        return hits
    else:
        return 0

def total_links():
    return Session.query(Link).count()

def total_categories():
    return Session.query(Category).count()

def total_searches():
    searches = Session.query(func.sum(SearchTerm.count)).one()[0]
    if searches:
        return searches
    else:
        return 0
