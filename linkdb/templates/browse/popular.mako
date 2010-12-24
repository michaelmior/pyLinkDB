##<%page cached="True" cache_key="popular-${str(c.pager.page)}" cache_timeout="300"/>
<%inherit file="/base.mako" />

<%def name="title()">
    Browsing Popular Links Page ${c.pager.page}
</%def>

<h2>Popular Links</h2>
${self.functions.show_links(c.pager)}
