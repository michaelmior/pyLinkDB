from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1272844988.963284
_template_filename='/home/mmior/src/linkdb/linkdb/templates/functions.mako'
_template_uri='/functions.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['show_pager', 'show_links']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n\n')
        # SOURCE LINE 31
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_show_pager(context,pager):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n<div class="pager">Page ')
        # SOURCE LINE 2
        __M_writer(escape(pager.pager(format='$link_first $link_previous ~2~ $link_next $link_last', page_param='page')))
        __M_writer(u' (showing ')
        __M_writer(escape(pager.first_item))
        __M_writer(u' to ')
        __M_writer(escape(pager.last_item))
        __M_writer(u' of ')
        __M_writer(escape(pager.item_count))
        __M_writer(u')</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_show_links(context,pager):
    context.caller_stack._push_frame()
    try:
        def show_pager(pager):
            return render_show_pager(context,pager)
        c = context.get('c', UNDEFINED)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n')
        # SOURCE LINE 6
        __M_writer(escape(show_pager(pager)))
        __M_writer(u'\n')
        # SOURCE LINE 7
        for link in pager.items:
            # SOURCE LINE 8
            __M_writer(u'<div class="link">\n    <a href="')
            # SOURCE LINE 9
            __M_writer(escape(h.url_for(controller='link', action='out', id=link.link_id)))
            __M_writer(u'" class="title">')
            __M_writer(escape(link.title))
            __M_writer(u'</a> <span class="url">')
            __M_writer(escape(link.url))
            __M_writer(u'</span>\n')
            # SOURCE LINE 10
            if c.admin:
                # SOURCE LINE 11
                __M_writer(u'        <a href="" class="delete" title="Delete">Delete</a>\n        <a href="')
                # SOURCE LINE 12
                __M_writer(escape(h.url_for(controller='link', action='edit', id=link.link_id)))
                __M_writer(u'" class="edit" title="Edit">Edit</a>\n')
            # SOURCE LINE 14
            __M_writer(u'    <p class="description">')
            __M_writer(escape(link.description))
            __M_writer(u'</p>\n    <div class="info">Added: ')
            # SOURCE LINE 15
            __M_writer(escape(link.date_added))
            __M_writer(u' &nbsp;Last Update: ')
            __M_writer(escape(link.date_updated))
            __M_writer(u' &nbsp;Category: <a href="')
            __M_writer(escape(h.url_for(controller='browse', action='categories', id=link.category.category_id, name=h.name_to_url(link.category.name))))
            __M_writer(u'">')
            __M_writer(escape(link.category.name))
            __M_writer(u'</a> &nbsp;Hits Out: ')
            __M_writer(escape(link.visit_count))
            __M_writer(u'</div>\n</div>\n')
        # SOURCE LINE 18
        __M_writer(u'\n')
        # SOURCE LINE 19
        __M_writer(escape(show_pager(pager)))
        __M_writer(u'\n\n<script type="text/javascript">\n$(document).ready(function() {\n  $(\'.link\').hover(function() {\n    $(\'a.delete, a.edit\', $(this)).show();\n  }, function() {\n    $(\'a.delete, a.edit\', $(this)).hide();\n  });\n});\n</script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


