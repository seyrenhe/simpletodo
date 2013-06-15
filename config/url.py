#!/usr/bin/env python
# coding: utf-8

pre_fix = 'controllers.'

urls = (
    '/',                    pre_fix + 'todo.Index',
    '/todo/new',            pre_fix + 'todo.New',
    '/todo/(\d+)',          pre_fix + 'todo.View',
    '/todo/(\d+)/edit',     pre_fix + 'todo.Edit',
    '/todo/(\d+)/delete',   pre_fix + 'todo.Delete',
    '/todo/(\d+)/finish',   pre_fix + 'todo.Finish',
    '/register',             pre_fix + 'login.Register',
    '/Admin',               pre_fix + 'todo.Admin',
    '/login',               pre_fix + 'login.Login',
    '/welcome',         pre_fix + 'login.welcome',
    '/logout',             pre_fix + 'login.Logout',

)
