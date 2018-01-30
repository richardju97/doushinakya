// server.js

var express = require("express");
var app = require("http")
var app = express();
var path = require('path');
var router = express.Router();
var http = require('http');
var bodyParser = require('body-parser');
var spawn = require("child_process").spawn;
//var path = __dirname + '/Angular/';
//var path2 = __dirname + '/Angular/template/';

router.use(function(req, res, next) {
	console.log("/" + req.method);
	next();
});

app.use(bodyParser.json());
app.use(bodyParser.urlencoded());

app.use('/', express.static(path.join(__dirname, '/Angular/')));

app.post('/conjugate', function(req, res) {
	console.log("got a get request for /conjugate");
//http.get('http://jisho.org/api/v1/search/words?keyword=oreo', (resp) => {
//  let data = '';

  // A chunk of data has been recieved.
//  resp.on('data', (chunk) => {
//    data += chunk;
//    console.log(data);
//  });
//});
/*
	var options = {
		host: "http://jisho.org/api/v1/search/words?keyword=oreo",
		method: 'GET',
		headers: {'Content-Type' : 'application/json'}
	}

	var temp = http.request(options, function(res) {

		console.log("Status: " + res.statusCode); 
		
	});
*/
	//console.log(res);
	/*
	res.on('data', function(chunk) {
		console.log("data: " + chunk);
	});
	//console.log(req);
	*/
	console.log(req['body']['verb']);
	var c = "";
	var py = spawn('python', ['conjugatefornode.py', 'oreo']);
	py.stdout.on('data', function(data) {
		console.log("got result back from python");
		console.log(data.toString());
	});	
});
//router.get("/", function(req, res){
//	res.sendFile(path + "index.html");
//});

//router.get("/about", function(req, res) {
//	res.sendFile(path + "about.html");
//});

app.use('/about', express.static(path.join(__dirname, '/Angular/')));

app.use('/contact', express.static(path.join(__dirname, '/Angular/')));

//router.get("/contact", function(req, res){
//	res.sendFile(path + "contact.html");
//});

//app.use("/", router);

app.use("*", function(req, res){
	res.sendFile(__dirname + "/Angular/template/404.html");
});

app.listen(process.env.PORT || 3000, function() {
	console.log("Live at Port 3000");
});
