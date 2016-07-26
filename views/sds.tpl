%def cssblock():

%end

%def jsblock():

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