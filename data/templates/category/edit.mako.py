from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1272836759.3835011
_template_filename='/home/mmior/src/linkdb/linkdb/templates/category/edit.mako'
_template_uri='/category/edit.mako'
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
        __M_writer(u'\n\n\n')
        # SOURCE LINE 4
        if c.category:
            # SOURCE LINE 5
            __M_writer(u'    ')
            # SOURCE LINE 7
            __M_writer(u'\n    ')
            # SOURCE LINE 8

            name = c.category.name
            button = 'Update'
                
            
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in ['button','name'] if __M_key in __M_locals_builtin()]))
            # SOURCE LINE 11
            __M_writer(u'\n')
            # SOURCE LINE 12
        else:
            # SOURCE LINE 13
            __M_writer(u'    ')
            # SOURCE LINE 15
            __M_writer(u'\n    ')
            # SOURCE LINE 16

            name = None
            button = 'Add'
                
            
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in ['button','name'] if __M_key in __M_locals_builtin()]))
            # SOURCE LINE 19
            __M_writer(u'\n')
        # SOURCE LINE 21
        __M_writer(u'\n<form name="category" class="jqtransform" action="')
        # SOURCE LINE 22
        __M_writer(escape(h.url_for(controller='category', action='save')))
        __M_writer(u'" method="post">\n    <div class="rowElem">\n        <label for="name">Name</label>\n        <input type="text" name="name" value="')
        # SOURCE LINE 25
        __M_writer(escape(name))
        __M_writer(u'" size="30" maxlength="255"/>\n    </div>\n\n')
        # SOURCE LINE 28
        if c.category:
            # SOURCE LINE 29
            __M_writer(u'    <input type="hidden" name="id" value="')
            __M_writer(escape(c.category.link_id))
            __M_writer(u'" />\n')
        # SOURCE LINE 31
        __M_writer(u'\n    <div class="rowElem lastrow">\n        <input type="submit" value="')
        # SOURCE LINE 33
        __M_writer(escape(button))
        __M_writer(u'"/><br/>\n        <a href="')
        # SOURCE LINE 34
        __M_writer(escape(h.url_for(controller='browse', action='categories')))
        __M_writer(u'" class="small">&laquo; Back</a>\n    </div>\n</form>\n\n\n<script type="text/javascript">\n$(document).ready(function() {\n  $(\'form.jqtransform\').jqTransform();\n});\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 13
        __M_writer(u'\n        Adding Category\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


