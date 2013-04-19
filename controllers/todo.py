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
tb = 'todo'
user = 'user'



def get_by_id(id):
    s = db.select(tb, where='id=$id', vars=locals())
    if not s:
        return False
    return s[0]

class New:

    def POST(self):
        i = web.input()
        title = i['title']
        if not title:
            return render.error('标题是必须的', None)
        db.insert(tb, title=title, post_date=datetime.now())
        raise web.seeother('/')


class Finish:

    def GET(self, id):
        todo = get_by_id(id)
        if not todo:
            return render.error('没找到这条记录', None)
        i = web.input()
        status = i.get('status', 'yes')
        if status == 'yes':
            finished = 1
        elif status == 'no':
            finished = 0
        else:
            return render.error('您发起了一个不允许的请求', '/')
        db.update(tb, finished=finished, where='id=$id', vars=locals())
        raise web.seeother('/')


class Edit:

    def GET(self, id):
        todo = get_by_id(id)
        if not todo:
            return render.error('没找到这条记录', None)
        return render.todo.edit(todo)

    def POST(self, id):
        todo = get_by_id(id)
        if not todo:
            return render.error('没找到这条记录', None)
        i = web.input()
        title = i['title']
        if not title:
            return render.error('标题是必须的', None)
        db.update(tb, title=title, where='id=$id', vars=locals())
        return render.error('修改成功！', '/')

class Delete:

    def GET(self, id):
        todo = get_by_id(id)
        if not todo:
            return render.error('没找到这条记录', None)
        db.delete(tb, where='id=$id', vars=locals())
        return render.error('删除成功！', '/')


class Index:

    def GET(self):
        todos1 = db.select(tb, order='finished asc, id asc',limit = 5)
        todos2 = db.select(tb, order='finished desc, id desc',limit = 5)

        return render.index(todos1,todos2)


class AddUser:

    def GET(self):
        return render.adduser()

    def POST():
        pass

class Login:

    def GET(self):
        return render.login()

    def POST():
        pass


class Admin:

    def GET():
        pass

    def POST():
        pass
