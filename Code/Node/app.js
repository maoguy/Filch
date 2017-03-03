var express = require ("express") ;
//var fs = require ("fs") ;
var userSetParameter = require ("./userSetParameter.js") ;

var app = express () ;

app.use (express.static("./static")) ;

app.get('/' , function(request , response){}) ;

app.get('/parameter' , userSetParameter) ;

var server = app.listen (3000 , function () {
  var host = server.address().address ;
  console.log (port) ;
  var port = server.address().port ;

  console.log ("Example app listening at http://%s:%s" , host , port) ;
}) ;
