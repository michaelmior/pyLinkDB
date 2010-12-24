<%inherit file="/base.mako" />

<%def name="title()">
    Login
</%def>

<form class="jqtransform" method="post" action="FORM_ACTION">
    <div class="rowElem">
        <label for="username">Username</label>
        <input type="text" name="username" length="30" maxlength="255" />
    </div>
    <div class="rowElem">
        <label for="password">Password</label>
        <input type="password" name="password" length="30" maxlength="255" />
    </div>
    <div class="rowElem lastrow">
        <button type="submit" name="authform" class="btn"><span><span>Login</span></span></button>
    </div>
</form>

<script type="text/javascript">
$(document).ready(function() {
  $('form.jqtransform').jqTransform();
});
</script>
