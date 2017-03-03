var fs = require ("fs") ;

module.exports = (request , response) => {
  var parameters = request.query ;
  //判断传感器类型,选择不同的文件路径
  var sensorType = parameters.sensorType ;
  var dirPath = "./PiCode/" + sensorType + "/";
  //获取用户自定义的参数
  var userApikey = parameters.apiKey ;
  var userPostTime = parameters.postTime ;
  var ScriptHeader = "#!/usr/bin/env python \n"+
  "#-*-coding:utf-8-*- \n" +
  "userApikey = '" + userApikey + "' \n" +
  "userPostTime = " + userPostTime + "\n" ;

  fs.readFile (dirPath + "pyScript.py" , "utf-8" ,
  (error , ScriptBody) => {
    if (error) {
      console.log (error) ;
    } else {
      //拼合数据并将数据写入新的脚本
      data =  ScriptHeader + ScriptBody;
      fs.writeFile (dirPath + sensorType + ".py" , data , "utf-8" ,
      (error) => {
        if (error) {
          console.log (error) ;
        } else {
          response.download (dirPath + sensorType + ".py") ;
          console.log("user download a" + sensorType + "Code") ;
        }
      })
    }
  })
}
