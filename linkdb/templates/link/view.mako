<%inherit file="/base.mako" />

<%def name="title()">
    Viewing Link ${c.link.title}
</%def>

<h2><a href="${c.link.url}">${c.link.title}</a></h2>

<p>${c.link.description}</p>
