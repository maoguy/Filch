#_*_coding:utf-8_*_
from flask import Flask , request ,render_template , session , url_for , redirect , flash
from flask_bootstrap import Bootstrap
from flask_script import Manager
#from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField
from wtforms.validators import Required
from datetime import datetime
from weatherQuery import weatherQuery
from pm25Query import getPM25 as pm25Query

#声明一个输入姓名文本框和提交按钮
class NameForm(FlaskForm):
    name = StringField('你的名字？',validators=[Required()])
    submit = SubmitField('提交')

class WeatherQueryForm (FlaskForm) :
    cityName = StringField ("你想知道广东的哪个城市天气？" , validators = [Required()] )
    submit = SubmitField ("查询")

class Pm25QueryForm (FlaskForm) :
    cityName = StringField ("你想知道哪个城市的实时空气质量指数(AQI)？" , validators = [Required()] )
    submit = SubmitField ("查询")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ni cai'
bootstrap = Bootstrap(app)#注意这个地方
#manager = Manager(app)
#moment = Moment(app)

@app.route ("/" , methods = ["GET" , "POST"])
def index():
    name = None
    nameForm = NameForm()

    #表单数据验证
    if nameForm.validate_on_submit() :
        name = nameForm.name.data
        nameForm.name.data = ""
        print (name)

    return render_template("index.html" , form = nameForm , name = name)

@app.route ("/test" , methods = ["GET" , "POST"])
def test () :
    return render_template ("index2.html")

@app.route ("/article" , methods = ["GET" , "POST"])
def article () :
    return render_template ("article.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

if __name__ == "__main__":
    app.run(host = '0.0.0.0' , debug = True , port = 5000)
