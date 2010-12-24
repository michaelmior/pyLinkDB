from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1272838765.7627881
_template_filename='/home/mmior/src/linkdb/linkdb/templates/browse/new.mako'
_template_uri='/browse/new.mako'
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
        context._push_buffer()
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        self = context.get('self', UNDEFINED)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 6
        __M_writer(u'\n\n<h2>Recent Links</h2>\n')
        # SOURCE LINE 9
        __M_writer(escape(self.functions.show_links(c.pager)))
        __M_writer(u'\n')
    finally:
        __M_buf = context._pop_buffer()
        context.caller_stack._pop_frame()
    return __M_buf.getvalue()


__M_render_body = render_body
def render_body(context,**pageargs):
    c = context.get('c', UNDEFINED)
    str = context.get('str', UNDEFINED)
    __M_writer = context.writer()
    __M_writer(context.get('local').get_cached('new-' + (str(c.pager.page)), defname='render_body', expiretime=300, createfunc=lambda:__M_render_body(context,**pageargs)))
    return ''
def render_title(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n    Browsing Recent Links Page ')
        # SOURCE LINE 5
        __M_writer(escape(c.pager.page))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


