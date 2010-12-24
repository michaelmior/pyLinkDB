from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1272853949.712954
_template_filename='/home/mmior/src/linkdb/linkdb/templates/link/edit.mako'
_template_uri='/link/edit.mako'
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
        __M_writer(u'\n\n')
        # SOURCE LINE 7
        if c.link:
            # SOURCE LINE 8

            id = c.link.link_id
            title = c.link.title
            url = c.link.url
            description = c.link.description
            button = 'Update'
            
            
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in ['url','description','button','id','title'] if __M_key in __M_locals_builtin()]))
            # SOURCE LINE 14
            __M_writer(u'\n')
            # SOURCE LINE 15
        else:
            # SOURCE LINE 16

            id = None
            title = ''
            url = ''
            description = ''
            button = 'Add'
            
            
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in ['url','description','button','id','title'] if __M_key in __M_locals_builtin()]))
            # SOURCE LINE 22
            __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(u'\n<form name="link" id="link" class="jqtransform" action="')
        # SOURCE LINE 25
        __M_writer(escape(h.url_for(controller='link', action='save', id=id)))
        __M_writer(u'" method="post">\n    <div class="rowElem">\n        <label for="title">Title</label>\n        <input type="text" name="title" value="')
        # SOURCE LINE 28
        __M_writer(escape(title))
        __M_writer(u'" size="30" maxlength="255"/>\n    </div>\n\n    <div class="rowElem">\n        <label for="url">URL</label>\n        <input type="text" name="url" value="')
        # SOURCE LINE 33
        __M_writer(escape(url))
        __M_writer(u'" size="30" maxlength="255"/>\n    </div>\n\n    <div class="rowElem">\n        <label for="category_id">Category</label>\n        <select name="category_id">\n')
        # SOURCE LINE 39
        if c.link:
            # SOURCE LINE 40
            __M_writer(u'            <option value="')
            __M_writer(escape(c.link.category.category_id))
            __M_writer(u'">')
            __M_writer(escape(c.link.category.name))
            __M_writer(u'</option>\n')
        # SOURCE LINE 42
        for category in c.categories:
            # SOURCE LINE 43
            if not (c.link and c.link.category.category_id == category.category_id):
                # SOURCE LINE 44
                __M_writer(u'            <option value="')
                __M_writer(escape(category.category_id))
                __M_writer(u'">')
                __M_writer(escape(category.name))
                __M_writer(u'</option>\n')
        # SOURCE LINE 47
        __M_writer(u'        </select>\n    </div>\n\n    <div class="rowElem">\n        <label for="description">Description</label>\n        <textarea rows="10" cols="35" name="description">')
        # SOURCE LINE 52
        __M_writer(escape(description))
        __M_writer(u'</textarea>\n    </div>\n\n    <input type="hidden" name="id" value="')
        # SOURCE LINE 55
        __M_writer(escape(id))
        __M_writer(u'" />\n\n    <div class="rowElem lastrow">\n        <input type="submit" value="')
        # SOURCE LINE 58
        __M_writer(escape(button))
        __M_writer(u'"/>\n    </div>\n\n</form>\n\n<script type="text/javascript">\n$(document).ready(function() {\n  $(\'form.jqtransform\').jqTransform();\n});\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    Editing Link\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


