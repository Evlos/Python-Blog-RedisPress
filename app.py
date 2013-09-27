#!/usr/bin/python
# -*- coding: utf-8 -*-

# RedisPress.alpha
# ---
# Database: Redis
# Framework: Tornado

import sys
import raven.contrib.tornado
import tornado.httpserver
import tornado.ioloop
import project.app.application

if __name__ == '__main__':
    if len(sys.argv) == 2:
        port = sys.argv[1]
    else:
        port = 24400
    sentry_key = '56b95038ef7849d7bfbfc735d2ee50e1:64c853d4c58947b5a8b663ca7ac2c8b1'
    app = project.app.application.Application()
    app.sentry_client = raven.contrib.tornado.AsyncSentryClient(
         'http://' + sentry_key + '@lin.eternalelf.com/sentry/7',
    )
    srv = tornado.httpserver.HTTPServer(app)
    srv.listen(int(port))
    tornado.ioloop.IOLoop.instance().start()
