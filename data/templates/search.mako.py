from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1272890509.1530709
_template_filename='/home/mmior/src/linkdb/linkdb/templates/search.mako'
_template_uri='/search.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 9
        __M_writer(u'\n')
        # SOURCE LINE 10
        if c.pager:
            # SOURCE LINE 11
            __M_writer(escape(self.functions.show_links(c.pager)))
            __M_writer(u'\n\n')
            # SOURCE LINE 13
        elif c.query:
            # SOURCE LINE 14
            __M_writer(u'<div class="flash">No results found for your query</div>\n')
        # SOURCE LINE 16
        __M_writer(u'\n')
        # SOURCE LINE 17
        if c.query:
            # SOURCE LINE 18
            __M_writer(escape(h.javascript_link('/js/jquery.highlight.js')))
            __M_writer(u'\n<script type="text/javascript">\n$(document).ready(function() {\n')
            # SOURCE LINE 21
            for word in c.query.split():
                # SOURCE LINE 22
                __M_writer(u"    $('.title').highlight('")
                __M_writer(escape(word))
                __M_writer(u"');\n    $('.description').highlight('")
                # SOURCE LINE 23
                __M_writer(escape(word))
                __M_writer(u"');\n")
            # SOURCE LINE 25
            __M_writer(u'});\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        if c.query:
            # SOURCE LINE 5
            __M_writer(u'    Searching for ')
            __M_writer(escape(c.query))
            __M_writer(u'\n')
            # SOURCE LINE 6
        else:
            # SOURCE LINE 7
            __M_writer(u'    Search\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


