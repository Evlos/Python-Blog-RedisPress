#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import raven.contrib.tornado
import tornado.web
import tornado.escape
import project.config


class Base(raven.contrib.tornado.SentryMixin, tornado.web.RequestHandler):
    def initialize(self):
        self.config = project.config
        self.loadtime = self._get_time()

    def esc(self, data):
        return tornado.escape.xhtml_escape(data)

    def esc_dict(self, di):
        for key, val in di.items():
            di[key] = self.esc(val)
        return di

    def get_current_user(self):
        return None

    def time_cost(self):
        return '%.3f ms' % ((self._get_times() - self.loadtime)*1000)

    def _get_times(self):
        return int(time.mktime(time.gmtime()))

    def _get_time(self):
        return time.time()


class Error(Base):
    def __init__(self, application, request, status_code):
        tornado.web.RequestHandler.__init__(self, application, request)
        self.set_status(status_code)

    def get_error_html(self, status_code, **kwargs):
        self.error = 'HTTP 404, Page not found'
        self.set_status(404)
        return self.render_string('error.html')
