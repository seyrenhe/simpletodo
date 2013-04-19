#!/usr/bin/env python
# coding: utf-8
from config.url import urls
import web

app = web.application(urls, globals())

if __name__ == "__main__":
    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app.run()
