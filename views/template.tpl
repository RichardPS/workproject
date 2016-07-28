<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <title>{{page_title}}</title>
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="favicon.ico" type="image/x-icon" />
    <link rel="stylesheet" type="text/css" href="style.css">
    %cssblock()
    <script type="text/javascript" src="jquery-3.1.0.min.js"></script>
    %jsblock()
</head>
<body>
<div class="container">
	<div class="inner-container">
		%headerblock()
		%contentblock()
		%footerblock()
	</div>
</div>
</body>
</html>