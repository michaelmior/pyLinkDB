from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1272804458.5748639
_template_filename='/home/mmior/src/linkdb/linkdb/templates/browse/letters.mako'
_template_uri='/browse/letters.mako'
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
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 6
        __M_writer(u'\n\n<ul id="letters" class="list">\n')
        # SOURCE LINE 9
        for letter in c.letters:
            # SOURCE LINE 10
            __M_writer(u'<li id="letter-')
            __M_writer(escape(letter.letter))
            __M_writer(u'"><a href="')
            __M_writer(escape(h.url_for(controller='browse', action='letters', id=letter.letter)))
            __M_writer(u'">')
            __M_writer(escape(letter.letter))
            __M_writer(u'</a> <span class="count">(')
            __M_writer(escape(letter.count_links()))
            __M_writer(u')</span></li>\n')
        # SOURCE LINE 12
        __M_writer(u'<ul>\n')
    finally:
        __M_buf = context._pop_buffer()
        context.caller_stack._pop_frame()
    return __M_buf.getvalue()


__M_render_body = render_body
def render_body(context,**pageargs):
    __M_writer = context.writer()
    __M_writer(context.get('local').get_cached('letters', defname='render_body', expiretime=300, createfunc=lambda:__M_render_body(context,**pageargs)))
    return ''
def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n    Viewing all Letters\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


