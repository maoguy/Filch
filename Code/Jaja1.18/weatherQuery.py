import requests
import json
from city import city

def weatherQuery (cityName) :
    cityCode = city.get(cityName) ;     #dict.get(key, default=None) 第二个参数为查找不成功的返回值
    if (cityCode != None) :
        url = ('http://www.weather.com.cn/data/cityinfo/%s.html') %cityCode

        response = requests.get(url)
        data = json.loads(response.content.decode('utf8'))
        result = data['weatherinfo']
        str_temp = ("%s %s %s ~ %s") % (result['city'] , result['weather'] , result['temp1'] , result['temp2'])

        return str_temp
    else :
        return None

def main () :
    cityName = input ("输入你想查询的广东省内的城市名 : ")
    weather = weatherQuery (cityName)
    if (weather != None) :
        print (weather)
    else :
        print ("输入有误!")

if __name__ == "__main__" :
    main ()
