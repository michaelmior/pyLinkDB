<%inherit file="/base.mako" />

<%def name="title()">
% if c.query:
    Searching for ${c.query}
% else:
    Search
% endif
</%def>
% if c.pager:
${self.functions.show_links(c.pager)}

% elif c.query:
<div class="flash">No results found for your query</div>
% endif

% if c.query:
${h.javascript_link('/js/jquery.highlight.js')}
<script type="text/javascript">
$(document).ready(function() {
    % for word in c.query.split():
    $('.title').highlight('${word}');
    $('.description').highlight('${word}');
    % endfor
});
</script>
% endif
