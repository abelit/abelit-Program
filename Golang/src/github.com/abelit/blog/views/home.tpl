<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Abelit's Home</title>
        <link rel="stylesheet" href="/static/css/home.css" type="text/css">
    </head>
    <body>
        <h1>Welcome to Abelit's Home Page</h1>
        <h2>About Author:</h2>
        <li>Name: {{ .name }}</li>
        <li>Email: {{ .email }}</li>
        <li>Website:<a href="{{ .website }}">{{ .website }}</a> </li>
    </body>
</html>
