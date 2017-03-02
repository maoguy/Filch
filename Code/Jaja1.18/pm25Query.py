#_*_coding:utf-8_*_
import urllib
import requests
import threading
import pinyin
from time import ctime
from bs4 import BeautifulSoup

def getPM25 (cityHanzi) :
	cityName = pinyin.get (cityHanzi , format = "strip" , delimiter = "")
	url = "http://www.pm25.com/" + cityName + ".html"

	html = urllib.request.urlopen (url)
	soup = BeautifulSoup (html , "html.parser")
	city = soup.find (class_ = "bi_loaction_city")	#城市名称
	aqi = soup.find ("a" , {"class" , "bi_aqiarea_num"})	#AQI指数
	quality = soup.select (".bi_aqiarea_right span")	#空气质量等级
	result = soup.find ("div" , class_ = 'bi_aqiarea_bottom')	#空气质量描述

	value = {}
	value["url"] = url
	value["city"] = city.text
	value["aqi"] = aqi.text
	value["quality"] = quality[0].text
	value["result"] = result.text
	value["time"] = ctime ()
	return value

def main () :
	cityName = input ("您想要查找哪个城市的空气质量: ")
	value = getPM25 (cityName)
	print (value["url"])
	print (value["city"])
	print (value["aqi"])
	print (value["quality"])
	print (value["result"])
	print (value["time"])

if __name__ == "__main__" :
	main ()
