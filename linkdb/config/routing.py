"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from pylons import config
from routes import Mapper

def make_map():
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE

    # Browsing routes
    map.connect('/browse/letters/{id}/page', controller='browse', action='letters')
    map.connect('/browse/letters/{id}/page/', controller='browse', action='letters')
    map.connect('/browse/letters/{id}/page/{page}', controller='browse', action='letters', page=1)

    map.connect('/browse/categories/{id}/{name}', controller='browse', action='categories', name=None)
    map.connect('/browse/categories/{id}/{name}/', controller='browse', action='categories', name=None)
    map.connect('/browse/categories/{id}/{name}/page', controller='browse', action='categories', name=None)
    map.connect('/browse/categories/{id}/{name}/page/', controller='browse', action='categories', name=None)
    map.connect('/browse/categories/{id}/{name}/page/{page}', controller='browse', action='categories', page=1)

    map.connect('/browse/new', controller='browse', action='new', page=1)
    map.connect('/browse/new/', controller='browse', action='new', page=1)
    map.connect('/browse/new/page', controller='browse', action='new', page=1)
    map.connect('/browse/new/page/', controller='browse', action='new', page=1)
    map.connect('/browse/new/page/{page}', controller='browse', action='new', page=1)

    map.connect('/browse/popular', controller='browse', action='popular', page=1)
    map.connect('/browse/popular/', controller='browse', action='popular', page=1)
    map.connect('/browse/popular/page', controller='browse', action='popular', page=1)
    map.connect('/browse/popular/page/', controller='browse', action='popular', page=1)
    map.connect('/browse/popular/page/{page}', controller='browse', action='popular', page=1)

    # Search route
    map.connect('/search', controller='search', action='search')
    map.connect('/search/', controller='search', action='search')
    map.connect('search', '/search')

    # Default routes
    map.connect('/{controller}/{action}')
    map.connect('/{controller}/{action}/{id}')
    map.connect('/{controller}/{action}/{id}/')

    return map
