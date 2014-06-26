#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of tornado_angular.
# https://github.com/heynemann/tornado-angular

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Bernardo Heynemann heynemann@gmail.com

import re

from tornado_angular.handlers import RequestHandler
from tornado_angular.serialize import dumps


class AngularHandler(RequestHandler):
    @property
    def config(self):
        return self.application.config

    def static_url(self, path):
        return "/web/%s" % (path.lstrip('/'))

    def get_template_namespace(self):
        namespace = super(AngularHandler, self).get_template_namespace()
        namespace['get_url'] = self.get_angular_url
        return namespace

    def get_angular_url(self, path):
        return "/web/%s" % (path.lstrip('/'))

    def render_path(self, path, **kwargs):
        template_path = self.application.config.ANGULAR_ROOT
        with RequestHandler._template_loader_lock:
            if template_path not in RequestHandler._template_loaders:
                loader = self.create_template_loader(template_path)
                RequestHandler._template_loaders[template_path] = loader
            else:
                loader = RequestHandler._template_loaders[template_path]
        t = loader.load(path)
        namespace = self.get_template_namespace()
        namespace.update(kwargs)
        return t.generate(**namespace)


class AngularIndexHandler(AngularHandler):
    def get(self):
        html = self.render_path("app/index.html")
        html = html.replace('<head>', '<head>\n    <base href="/web/" />')
        self.finish(html)


class AngularViewHandler(AngularHandler):
    def get(self, path):
        html = self.render_path("app/views/%s" % path)
        self.finish(html)


class AngularRedirectHandler(AngularIndexHandler):
    def get(self, url):
        if url == "web/":
            super(AngularRedirectHandler, self).get()
            return

        url = re.sub(r"^/?web/?", "", url)

        self.redirect("/web/%s" % url.lstrip('/'))


class AngularConfigHandler(AngularIndexHandler):
    def to_camel(self, name):
        capital = "".join([word.strip().capitalize() for word in name.split('_') if word])
        return "%s%s" % (capital[0].lower(), "".join(capital[1:]))

    def get(self):
        items = []

        for config in self.application.allowed_configuration:
            items.append("%s: %s" % (self.to_camel(config), dumps(self.config[config])))

        template = """
'use strict';
angular.module('%s').constant('ConfigConst', {
%s
});
        """.strip('') % (
            self.application.web_app_name,
            ",\n".join(items)
        )
        self.write(template)
        self.finish()
