from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1272890462.3217831
_template_filename='/home/mmior/src/linkdb/linkdb/templates/base.mako'
_template_uri='/base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['stats']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 1
    ns = runtime.Namespace('functions', context._clean_inheritance_tokens(), templateuri='/functions.mako', callables=None, calling_uri=_template_uri, module=None)
    context['self'].functions = ns
    context.namespaces[(__name__, 'functions')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'functions')._populate(_import_ns, ['*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        def stats():
            return render_stats(context.locals_(__M_locals))
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        next = _import_ns.get('next', context.get('next', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n<!DOCTYPE html>\n<html>\n    <head>\n        <meta http-equiv="Content-Type" content="text/html;charset=utf8" />\n        <title>')
        # SOURCE LINE 6
        __M_writer(escape(self.title()))
        __M_writer(u' - Community College and Higher Education Research Links (CCORL)</title>\n        ')
        # SOURCE LINE 7
        __M_writer(escape(h.stylesheet_link('/styles.css')))
        __M_writer(u'\n        ')
        # SOURCE LINE 8
        __M_writer(escape(h.stylesheet_link('/jqtransform.css')))
        __M_writer(u'\n        <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>\n        ')
        # SOURCE LINE 10
        __M_writer(escape(h.javascript_link('/js/jquery.jqtransform.js')))
        __M_writer(u'\n    </head>\n    <body>\n        <div id="header">\n            <h1>Community College and Higher Education Research Links</h1>\n            <form name="search" id="search" action="')
        # SOURCE LINE 15
        __M_writer(escape(h.url_for('search')))
        __M_writer(u'">\n                <label for="query">Search</label><br/>\n')
        # SOURCE LINE 17
        if c.query:
            # SOURCE LINE 18
            __M_writer(u'                    <input name="query" length="20" value="')
            __M_writer(escape(c.query))
            __M_writer(u'"/>\n')
            # SOURCE LINE 19
        else:
            # SOURCE LINE 20
            __M_writer(u'                    <input name="query" length="20"/>\n')
        # SOURCE LINE 22
        __M_writer(u'                <button type="submit" title="Search">Search</button>\n            </form>\n            <hr/>\n            <div id="menu">\n                <span>View Links by:</span>\n                <ul id="menu">\n                    <li><a href="')
        # SOURCE LINE 28
        __M_writer(escape(h.url_for(controller='browse', action='categories')))
        __M_writer(u'">Category</a></li>\n                    <li><a href="')
        # SOURCE LINE 29
        __M_writer(escape(h.url_for(controller='browse', action='letters')))
        __M_writer(u'">Letter</a></li>\n                    <li><a href="')
        # SOURCE LINE 30
        __M_writer(escape(h.url_for(controller='browse', action='popular')))
        __M_writer(u'">Popularity</a></li>\n                    <li><a href="')
        # SOURCE LINE 31
        __M_writer(escape(h.url_for(controller='browse', action='new')))
        __M_writer(u'">Recency</a></li>\n')
        # SOURCE LINE 32
        if c.admin:
            # SOURCE LINE 33
            __M_writer(u'                    <li id="logout"><a href="')
            __M_writer(escape(h.url_for(controller='users', action='logout')))
            __M_writer(u'">Logout</a></li>\n')
        # SOURCE LINE 35
        __M_writer(u'                </ul>\n            </div>\n            <hr/>\n        </div>\n        <div id="container">\n')
        # SOURCE LINE 40
        if c.flash:
            # SOURCE LINE 41
            __M_writer(u'            <div class="flash">')
            __M_writer(escape(c.flash))
            __M_writer(u'</div>\n')
        # SOURCE LINE 43
        __M_writer(u'            ')
        __M_writer(escape(next.body()))
        __M_writer(u'\n        </div>\n        <div id="footer">\n            <hr/>\n            ')
        # SOURCE LINE 49
        __M_writer(u'\n            ')
        # SOURCE LINE 50
        __M_writer(escape(stats()))
        __M_writer(u'\n        </div>\n')
        # SOURCE LINE 52
        if c.admin:
            # SOURCE LINE 53
            __M_writer(u'        <script type="text/javascript">\n        $(document).ready(function() {\n          $(\'a.delete, a.edit\').hide()\n        });\n        </script>\n')
        # SOURCE LINE 59
        __M_writer(u'    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stats(context):
    context.caller_stack._push_frame()
    try:
        context._push_buffer()
        _import_ns = {}
        _mako_get_namespace(context, 'functions')._populate(_import_ns, ['*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 47
        __M_writer(u'\n            Total Categories: ')
        # SOURCE LINE 48
        __M_writer(escape(h.stats.total_categories()))
        __M_writer(u' Total Links: ')
        __M_writer(escape(h.stats.total_links()))
        __M_writer(u' Searches Performed: ')
        __M_writer(escape(h.stats.total_searches()))
        __M_writer(u' Hits Out: ')
        __M_writer(escape(h.stats.total_hits()))
        __M_writer(u'\n            ')
    finally:
        __M_buf = context._pop_buffer()
        context.caller_stack._pop_frame()
    return __M_buf.getvalue()


__M_render_stats = render_stats
def render_stats(context):
    _import_ns = {}
    _mako_get_namespace(context, 'functions')._populate(_import_ns, ['*'])
    __M_writer = context.writer()
    __M_writer(context.get('local').get_cached('stats', defname='render_stats', expiretime=300, type='file', createfunc=lambda:__M_render_stats(context)))
    return ''
