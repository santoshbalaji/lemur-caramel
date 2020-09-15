var express = require('express');
var app = express();

app.use(express.static('public/js'))

app.get('/task', function(req, res) {
	res.sendFile(__dirname + '/public/html/task.html');
});

app.get('*', function(req, res)
{
	res.sendFile(__dirname + '/public/html/404.html');
});

app.listen(3001);

