<%page cached="True" cache_key="new-${str(c.pager.page)}" cache_timeout="300"/>
<%inherit file="/base.mako" />

<%def name="title()">
    Browsing Recent Links Page ${c.pager.page}
</%def>

<h2>Recent Links</h2>
${self.functions.show_links(c.pager)}
