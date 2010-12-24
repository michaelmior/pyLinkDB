from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1272893246.6440799
_template_filename='/home/mmior/src/linkdb/linkdb/templates/browse/categories.mako'
_template_uri='/browse/categories.mako'
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
        __M_writer(u'\n\n<a href="')
        # SOURCE LINE 8
        __M_writer(escape(h.url_for(controller='category', action='edit')))
        __M_writer(u'" class="add">Add a Category</a>\n\n<ul id="categories" class="list">\n')
        # SOURCE LINE 11
        for category in c.categories:
            # SOURCE LINE 12
            __M_writer(u'<li id="category-')
            __M_writer(escape(category.category_id))
            __M_writer(u'"><a href="')
            __M_writer(escape(h.url_for(controller='browse', action='categories', id=category.category_id)))
            __M_writer(u'">')
            __M_writer(escape(category.name))
            __M_writer(u'</a> <span class="count">(')
            __M_writer(escape(category.count_links()))
            __M_writer(u')\n')
            # SOURCE LINE 13
            if c.admin and category.category_id != 1:
                # SOURCE LINE 14
                __M_writer(u'<a href="')
                __M_writer(escape(h.url_for(controller='category', action='delete', id=category.category_id)))
                __M_writer(u'" class="delete" title="Delete">Delete</a>\n<a href="')
                # SOURCE LINE 15
                __M_writer(escape(h.url_for(controller='category', action='edit', id=category.category_id)))
                __M_writer(u'" class="edit" title="Edit">Edit</a>\n')
            # SOURCE LINE 17
            __M_writer(u'\n</span></li>\n')
        # SOURCE LINE 20
        __M_writer(u'<ul>\n\n<script type="text/javascript">\n$(document).ready(function() {\n  $(\'a.delete, a.edit\').hide()\n  $(\'ul#categories li\').hover(function() {\n    $(\'a.delete, a.edit\').show()\n  }, function() {\n    $(\'a.delete, a.edit\').hide()\n  });\n  $(\'.delete\').click(function() {\n    li = $(this).parents(\'li\').first()[0];\n    id = li.id.split(\'-\')[1];\n    $.ajax({\n      type: \'GET\',\n      url: \'delete/\'+id,\n      cache: false,\n      success: function() {\n        $(li).remove();\n      }\n    });\n    return false;\n  });\n});\n</script>\n')
    finally:
        __M_buf = context._pop_buffer()
        context.caller_stack._pop_frame()
    return __M_buf.getvalue()


__M_render_body = render_body
def render_body(context,**pageargs):
    __M_writer = context.writer()
    __M_writer(context.get('local').get_cached('categories', defname='render_body', expiretime=300, createfunc=lambda:__M_render_body(context,**pageargs)))
    return ''
def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n    Viewing all Categories\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


