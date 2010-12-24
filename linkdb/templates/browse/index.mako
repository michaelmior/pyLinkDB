<%inherit file="/base.mako"/>

<%def name="title()">
    View Links
</%def>

<ul>
% for category in c.categories:
    <li><a href="${h.url_for(controller='browse', action='category', id=category.id)}">${category.name}</a></li>
% endfor
<ul>
