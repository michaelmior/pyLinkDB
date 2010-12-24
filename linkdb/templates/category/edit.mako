<%inherit file="/base.mako"/>


% if c.category:
    <%def name="title()">
        Edting Category
    </%def>
    <%
        name = c.category.name
        button = 'Update'
    %>
% else:
    <%def name="title()">
        Adding Category
    </%def>
    <%
        name = None
        button = 'Add'
    %>
% endif

<form name="category" class="jqtransform" action="${h.url_for(controller='category', action='save')}" method="post">
    <div class="rowElem">
        <label for="name">Name</label>
        <input type="text" name="name" value="${name}" size="30" maxlength="255"/>
    </div>

    % if c.category:
    <input type="hidden" name="id" value="${c.category.link_id}" />
    % endif

    <div class="rowElem lastrow">
        <input type="submit" value="${button}"/><br/>
        <a href="${h.url_for(controller='browse', action='categories')}" class="small">&laquo; Back</a>
    </div>
</form>


<script type="text/javascript">
$(document).ready(function() {
  $('form.jqtransform').jqTransform();
});
</script>
