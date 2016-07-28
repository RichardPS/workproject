%def cssblock():
<link rel="stylesheet" type="text/css" href="index.css">
%end

%def jsblock():
<script type="text/javascript" src="common.js"></script>
%end

%def headerblock():
<div class="header">
&nbsp;
</div>
%end

%def contentblock():
<div class="content">
&nbsp;
</div>
%end

%def footerblock():
<div class="footer">
&nbsp;
</div>
%end

%rebase template cssblock=cssblock, jsblock=jsblock, headerblock=headerblock, contentblock=contentblock, footerblock= footerblock