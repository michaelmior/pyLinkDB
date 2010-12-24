<%page cached="True" cache_key="categories" cache_timeout="300"/>
<%inherit file="/base.mako"/>

<%def name="title()">
    Viewing all Categories
</%def>

<a href="${h.url_for(controller='category', action='edit')}" class="add">Add a Category</a>

<ul id="categories" class="list">
% for category in c.categories:
<li id="category-${category.category_id}"><a href="${h.url_for(controller='browse', action='categories', id=category.category_id)}">${category.name}</a> <span class="count">(${category.count_links()})
% if c.admin and category.category_id != 1:
<a href="${h.url_for(controller='category', action='delete', id=category.category_id)}" class="delete" title="Delete">Delete</a>
<a href="${h.url_for(controller='category', action='edit', id=category.category_id)}" class="edit" title="Edit">Edit</a>
% endif

</span></li>
% endfor
<ul>

<script type="text/javascript">
$(document).ready(function() {
  $('a.delete, a.edit').hide()
  $('ul#categories li').hover(function() {
    $('a.delete, a.edit').show()
  }, function() {
    $('a.delete, a.edit').hide()
  });
  $('.delete').click(function() {
    li = $(this).parents('li').first()[0];
    id = li.id.split('-')[1];
    $.ajax({
      type: 'GET',
      url: 'delete/'+id,
      cache: false,
      success: function() {
        $(li).remove();
      }
    });
    return false;
  });
});
</script>
