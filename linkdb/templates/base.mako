<%namespace name="functions" file="/functions.mako" import="*" inheritable="True"/>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=utf8" />
        <title>${self.title()} - pyLinkDB</title>
        ${h.stylesheet_link('/styles.css')}
        ${h.stylesheet_link('/jqtransform.css')}
        <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
        ${h.javascript_link('/js/jquery.jqtransform.js')}
    </head>
    <body>
        <div id="header">
            <h1>pyLinkDB</h1>
            <form name="search" id="search" action="${h.url_for('search')}">
                <label for="query">Search</label><br/>
                % if c.query:
                    <input name="query" length="20" value="${c.query}"/>
                % else:
                    <input name="query" length="20"/>
                % endif
                <button type="submit" title="Search">Search</button>
            </form>
            <hr/>
            <div id="menu">
                <span>View Links by:</span>
                <ul id="menu">
                    <li><a href="${h.url_for(controller='browse', action='categories')}">Category</a></li>
                    <li><a href="${h.url_for(controller='browse', action='letters')}">Letter</a></li>
                    <li><a href="${h.url_for(controller='browse', action='popular')}">Popularity</a></li>
                    <li><a href="${h.url_for(controller='browse', action='new')}">Recency</a></li>
                    % if c.admin:
                    <li id="logout"><a href="${h.url_for(controller='users', action='logout')}">Logout</a></li>
                    % endif
                </ul>
            </div>
            <hr/>
        </div>
        <div id="container">
            % if c.flash:
            <div class="flash">${c.flash}</div>
            % endif
            ${next.body()}
        </div>
        <div id="footer">
            <hr/>
            <%def name="stats()" cached="True" cache_key="stats" cache_timeout="300" cache_type="file">
            Total Categories: ${h.stats.total_categories()} Total Links: ${h.stats.total_links()} Searches Performed: ${h.stats.total_searches()} Hits Out: ${h.stats.total_hits()}
            </%def>
            ${stats()}
        </div>
        % if c.admin:
        <script type="text/javascript">
        $(document).ready(function() {
          $('a.delete, a.edit').hide()
        });
        </script>
        % endif
    </body>
</html>
