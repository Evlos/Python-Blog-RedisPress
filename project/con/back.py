#!/usr/bin/python
# -*- coding: utf-8 -*-

import project.con.controllers


class Compose(project.con.controllers.Base):
    def get(self):
        self.render('back/compose.html')
