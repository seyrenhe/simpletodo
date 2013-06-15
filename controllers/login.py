#!/usr/bin/env python
# coding: utf-8
import web 
from config import settings
from datetime import datetime
import sys
reload(sys) #python初始化后会删除sys.setdefaultencoding方法,需要重新载入sys模块来使用这个方法.
sys.setdefaultencoding('utf-8')

render = settings.render
db = settings.db

class Login:
    def GET(self):
        name= web.cookies().get('have_user')
        if name :
            return web.seeother('/welcome')
        return render.login()

    
    def POST(self):
        i=web.input()
        name=i['username']
        pwd=i['password']
        ident = db.query("select * from user where user ='%s'" %(name))
        if not ident :
            return "<html><body><p>用户不存在！</p><a href='/login'>返回登录页</a></body></html>"
        else:
            if ident[0]['password']==pwd :
                web.setcookie('have_user',name,3600)
                return web.seeother('/welcome')
            else:
                return "<html><body><p>用户名或密码错误！</p><a href='/login'>返回登录页</a></body></html>"




class Logout:
    def GET(self):
        name=web.cookies().get('have_user')
        web.setcookie('have_user',name,-1)
        #return "<html><head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" /></head><body><a href='/'>返回首页</a><br><a href='/login'>返回登录</a></body></html>"
        return render.bye(name)



class welcome:
    def GET(self):
        name=web.cookies().get('have_user')
        if not name :
            return web.seeother('/login')
        return render.welcome(name)



class Register:
    def GET(self):
        return render.register()
    def POST(self):
        i=web.input()
        name=i['name']
        pwd1=i['pwd1']
        pwd2=i['pwd2']
        email = i['email']
        ident = db.query("select * from user where user='%s'" %(name))
        if ident :
            return "<html><body><p>用用户已存在！</p><a href='/login'>返回登录页面</a></body></html>"
        else :
            db.insert('user',user=name,password=pwd1,email=email)
            return "<html><body><p>注册成功！</p><a href='/login'>返回登录页面</a></body></html>"
