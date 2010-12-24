from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1272261798.5612481
_template_filename='/home/mmior/src/linkdb/linkdb/templates/browse/index.mako'
_template_uri='/browse/index.mako'
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
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n<ul>\n')
        # SOURCE LINE 8
        for category in c.categories:
            # SOURCE LINE 9
            __M_writer(u'    <li><a href="')
            __M_writer(escape(h.url_for(controller='browse', action='category', id=category.id)))
            __M_writer(u'">')
            __M_writer(escape(category.name))
            __M_writer(u'</a></li>\n')
        # SOURCE LINE 11
        __M_writer(u'<ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    View Links\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


