<%inherit file="/base.mako"/>

<%def name="title()">
    Editing Link
</%def>

% if c.link:
<%
id = c.link.link_id
title = c.link.title
url = c.link.url
description = c.link.description
button = 'Update'
%>
% else:
<%
id = None
title = ''
url = ''
description = ''
button = 'Add'
%>
% endif

<form name="link" id="link" class="jqtransform" action="${h.url_for(controller='link', action='save', id=id)}" method="post">
    <div class="rowElem">
        <label for="title">Title</label>
        <input type="text" name="title" value="${title}" size="30" maxlength="255"/>
    </div>

    <div class="rowElem">
        <label for="url">URL</label>
        <input type="text" name="url" value="${url}" size="30" maxlength="255"/>
    </div>

    <div class="rowElem">
        <label for="category_id">Category</label>
        <select name="category_id">
        % if c.link:
            <option value="${c.link.category.category_id}">${c.link.category.name}</option>
        % endif
        % for category in c.categories:
            % if not (c.link and c.link.category.category_id == category.category_id):
            <option value="${category.category_id}">${category.name}</option>
            % endif
        % endfor
        </select>
    </div>

    <div class="rowElem">
        <label for="description">Description</label>
        <textarea rows="10" cols="35" name="description">${description}</textarea>
    </div>

    <input type="hidden" name="id" value="${id}" />

    <div class="rowElem lastrow">
        <input type="submit" value="${button}"/>
    </div>

</form>

<script type="text/javascript">
$(document).ready(function() {
  $('form.jqtransform').jqTransform();
});
</script>
