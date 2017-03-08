<!DOCTYPE HTML>
<html>
  <head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta charset="utf-8">
    <title>${title}</title>
    % for keyword in keywords:
      <meta name="keywords" content=${keyword}>
    % endfor
    <meta name="description" content=${description}>
    <meta name="author" content=${email}>
    <!--Import Google Icon Font-->
    <link href="http://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <!--Import materialize.css-->
    % if debug:
      <link href="//cdn.bootcss.com/materialize/0.98.0/css/materialize.css" rel="stylesheet">
    % else:
      <link href="//cdn.bootcss.com/materialize/0.98.0/css/materialize.min.css" rel="stylesheet">
    % endif
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  </head>
  <body>
    <header class="header">
      <%block name="header">
        fake header
      </%block>
    </header>
    ${self.body()}
    <footer class="footer">
      <%block name="footer">
        fake footer
      </%block>
    </footer>
    <!--Import jQuery before materialize.js-->
    % if debug:
      <script src="//cdn.bootcss.com/jquery/2.1.1/jquery.js"></script>
      <script src="//cdn.bootcss.com/materialize/0.98.0/js/materialize.js"></script>
    % else:
      <script src="//cdn.bootcss.com/jquery/2.1.1/jquery.min.js"></script>
      <script src="//cdn.bootcss.com/materialize/0.98.0/js/materialize.min.js"></script>
    % endif
  </body>
</html>
