
import RPi.GPIO as GPIO
import time
import json
import requests
import os

#采用BCM编号方式，对应4
channel = 4 ;
data = [] ;
j = 0 ;

#I/O口使用BCM编号方式
GPIO.setmode (GPIO.BCM) ;

time.sleep (1) ;

#设置数据线为输出
GPIO.setup (channel , GPIO.OUT) ;

GPIO.output (channel , GPIO.LOW) ;
time.sleep (0.02) ;
GPIO.output (channel , GPIO.HIGH) ;

#设置数据线为输入
GPIO.setup (channel , GPIO.IN) ;

while GPIO.input (channel) == GPIO.LOW :
    continue ;

while GPIO.input (channel) == GPIO.HIGH :
    continue ;

while j < 40 :
    k = 0 ;
    while GPIO.input (channel) == GPIO.LOW :
        continue ;

    while GPIO.input (channel) == GPIO.HIGH :
        k += 1 ;
        if k > 100 :
            break ;

    if k < 8 :
        data.append (0) ;
    else :
        data.append (1) ;

    j += 1 ;

print "sensor is working ! " ;
print data ;

#读取数值
humidity_bit = data[0:8] ;
humidity_point_bit = data[8:16] ;
temperature_bit = data[16:24] ;
temperature_point_bit = data[24:32] ;
check_bit = data[32:40] ;

humidity = 0 ;
humidity_point = 0 ;
temperature = 0 ;
temperature_point = 0 ;
check = 0 ;

#数值转换
for i in range (8) :
    humidity += humidity_bit[i] * 2 ** (7 - i) ;
    humidity_point += humidity_point_bit[i] * 2 ** (7 - i) ;
    temperature += temperature_bit[i] * 2 ** (7 - i) ;
    temperature_point += temperature_point_bit[i] * 2 ** (7 - i) ;
    check += check_bit[i] * 2 ** (7 - i) ;

tmp = humidity + humidity_point + temperature + temperature_point ;

#数据校验
if check == tmp :
    print "temperature : " , temperature , ", humidity : " , humidity ;
else :
    print "wrong ! " ;
    print "temperature : " , temperature , ", humidity : " , humidity , "check : ", check , "tmp : ", tmp ;

GPIO.cleanup () ;

#上传数据到服务器

#数据转换成JSON格式
mytemp = {"value" : temperature}  ;
myhumi = {"value" : humidity}  ;

#传感器URL
tempUrl = 'http://api.yeelink.net/v1.0/device/349731/sensor/392015/datapoints' ;
humiUrl = 'http://api.yeelink.net/v1.0/device/349731/sensor/392056/datapoints' ;

#apikey
apikey = "Apikey" ;
postTime = 5 ;  #默认上报时间间隔为5分钟

#若用户自定义了apikey，则替换之
if userApikey :
    apikey = userApikey ;

#若用户自定义了上传时间间隔，则替换之
if  userPostTime :
    postTime = int(userPostTime) ;

#headers
apiheaders = {'U-ApiKey':apikey , 'content-type' : 'application/json'} ;

#发送请求
if check == tmp :
    temp = requests.post (tempUrl , headers = apiheaders , data = json.dumps(mytemp)) ;
    humi = requests.post (humiUrl , headers = apiheaders , data = json.dumps(myhumi)) ;
    print ("data has uploaded") ;

    time.sleep (5*int(time)) ;
else :
    print ("data ERROR!") ;

print ("NEXT -->") ;    
