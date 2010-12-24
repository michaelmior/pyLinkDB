<%page cached="True" cache_key="letter-${c.letter}-${str(c.pager.page)}" cache_timeout="300"/>
<%inherit file="/base.mako" />

<%def name="title()">
    Browsing Letter ${c.letter} Page ${c.pager.page}
</%def>

<h2>Letter ${c.letter}</h2>
${self.functions.show_links(c.pager)}
