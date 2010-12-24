<%def name="show_pager(pager)">
<div class="pager">Page ${pager.pager(format='$link_first $link_previous ~2~ $link_next $link_last', page_param='page')} (showing ${pager.first_item} to ${pager.last_item} of ${pager.item_count})</div>
</%def>

<%def name="show_links(pager)">
${show_pager(pager)}
% for link in pager.items:
<div class="link">
    <a href="${h.url_for(controller='link', action='out', id=link.link_id)}" class="title">${link.title}</a> <span class="url">${link.url}</span>
    % if c.admin:
        <a href="" class="delete" title="Delete">Delete</a>
        <a href="${h.url_for(controller='link', action='edit', id=link.link_id)}" class="edit" title="Edit">Edit</a>
    % endif
    <p class="description">${link.description}</p>
    <div class="info">Added: ${link.date_added} &nbsp;Last Update: ${link.date_updated} &nbsp;Category: <a href="${h.url_for(controller='browse', action='categories', id=link.category.category_id, name=h.name_to_url(link.category.name))}">${link.category.name}</a> &nbsp;Hits Out: ${link.visit_count}</div>
</div>
% endfor

${show_pager(pager)}

<script type="text/javascript">
$(document).ready(function() {
  $('.link').hover(function() {
    $('a.delete, a.edit', $(this)).show();
  }, function() {
    $('a.delete, a.edit', $(this)).hide();
  });
});
</script>

</%def>
