#!/usr/bin/python
# -*- coding: utf-8 -*-

import os.path
import tornado.web
import project.config
import project.con.controllers


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', project.con.controllers.Index),
        ]
        settings = {
            'template_path': os.path.join(os.path.dirname(__file__), '../../template'),
            'static_path': os.path.join(os.path.dirname(__file__), '../../static'),
            'xsrf_cookies': True,
            'cookie_secret': project.config.keys['cookie'],
            'login_url': '/login/',
            'autoescape': None,
            'title': project.config.sets['title'],
            'url': project.config.sets['url'],
            'debug': False,
        }
        tornado.web.Application.__init__(self, handlers, **settings)
        tornado.web.ErrorHandler = project.con.controllers.Error
