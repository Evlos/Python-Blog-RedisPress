#!/usr/bin/python
# -*- coding: utf-8 -*-

import project.con.controllers


class Index(project.con.controllers.Base):
    def get(self):
        self.render('front/index.html')


class Article(project.con.controllers.Base):
    def get(self, aid):
        self.render('front/article.html')
