<%page cached="True" cache_key="letters" cache_timeout="300" />
<%inherit file="/base.mako"/>

<%def name="title()">
    Viewing all Letters
</%def>

<ul id="letters" class="list">
% for letter in c.letters:
<li id="letter-${letter.letter}"><a href="${h.url_for(controller='browse', action='letters', id=letter.letter)}">${letter.letter}</a> <span class="count">(${letter.count_links()})</span></li>
% endfor
<ul>
