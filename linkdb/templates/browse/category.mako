<%page cached="True" cache_key="category-${c.category.name}-page-${str(c.pager.page)}" cache_timeout="300"/>
<%inherit file="/base.mako" />

<%def name="title()">
    Browsing Category ${c.category.name} Page ${c.pager.page}
</%def>

<h2>Category ${c.category.name}</h2>
${self.functions.show_links(c.pager)}
