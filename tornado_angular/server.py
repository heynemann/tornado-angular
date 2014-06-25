#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of tornado_angular.
# https://github.com/heynemann/tornado-angular

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Bernardo Heynemann heynemann@gmail.com

from os.path import abspath, join

from cow.server import Server
from tornado.httpclient import AsyncHTTPClient
import tornado.web

from tornado_angular import __version__
from tornado_angular.handlers import RequestHandler
from tornado_angular.handlers.angular_handler import AngularIndexHandler, AngularRedirectHandler
from tornado_angular.config import Config


def main():
    AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")
    TornadoAngularServer.run()


class VersionHandler(RequestHandler):
    def get_version(self):
        return __version__

    def get(self):
        self.write(self.get_version())


class TornadoAngularServer(Server):
    def __init__(self, debug=None, *args, **kw):
        super(TornadoAngularServer, self).__init__(*args, **kw)
        self.force_debug = debug

    def get_extra_server_parameters(self):
        return {
            'no_keep_alive': False
        }

    def initialize_app(self, *args, **kw):
        super(TornadoAngularServer, self).initialize_app(*args, **kw)

        if self.force_debug is not None:
            self.debug = self.force_debug

    def get_api_handlers(self):
        return [
            ('bla/?', VersionHandler),
        ]

    def get_api_prefix(self):
        return "api"

    def get_web_handlers(self):
        angular_path = abspath(self.config.ANGULAR_ROOT)
        
        items = (
            ('bower_components', join(angular_path, 'bower_components')),
            ('scripts', join(angular_path, '.tmp/scripts')),
            ('styles', join(angular_path, '.tmp/styles')),
            ('images', join(angular_path, 'app/images')),
            ('views', join(angular_path, 'app/views'))
        )

        handlers = []

        for url, path in items:
            handlers.append((r"/web/%s/(.+)" % url, tornado.web.StaticFileHandler, {'path': path}))

        handlers.append((r'/web/.+', AngularIndexHandler))

        return handlers

    def get_handlers(self):
        handlers = [
            ('/version/?', VersionHandler),
        ]

        api_handlers = list(self.get_api_handlers())
        api_prefix = self.get_api_prefix()

        for api_handler in api_handlers:
            handler = list(api_handler)
            handler[0] = r"/%s/%s" % (api_prefix, handler[0])
            handlers.append(handler)

        handlers.append(
            ('/(.*)', AngularRedirectHandler),
        )

        return tuple(self.get_web_handlers() + handlers)

    def get_config(self):
        return Config

    def get_api_plugins(self):
        return []

    def get_plugins(self):
        return self.get_api_plugins()

    def api_after_start(self, io_loop):
        pass

    def after_start(self, io_loop):
        self.api_after_start(io_loop)

    def api_before_end(self, io_loop):
        pass

    def before_end(self, io_loop):
        self.api_before_end(io_loop)

if __name__ == '__main__':
    main()
