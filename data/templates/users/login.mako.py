from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1272247434.041805
_template_filename='/home/mmior/src/linkdb/linkdb/templates/users/login.mako'
_template_uri='/users/login.mako'
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
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n<form class="jqtransform" method="post" action="FORM_ACTION">\n    <div class="rowElem">\n        <label for="username">Username</label>\n        <input type="text" name="username" length="30" maxlength="255" />\n    </div>\n    <div class="rowElem">\n        <label for="password">Password</label>\n        <input type="password" name="password" length="30" maxlength="255" />\n    </div>\n    <div class="rowElem lastrow">\n        <button type="submit" name="authform" class="btn"><span><span>Login</span></span></button>\n    </div>\n</form>\n\n<script type="text/javascript">\n$(document).ready(function() {\n  $(\'form.jqtransform\').jqTransform();\n});\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    Login\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


