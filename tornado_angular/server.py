#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of tornado_angular.
# https://github.com/heynemann/tornado-angular

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Bernardo Heynemann heynemann@gmail.com

import sys
from os.path import abspath, join

from cow.server import Server
import cow.handlers.healthcheck as healthcheck
from tornado.httpclient import AsyncHTTPClient
import tornado.web

from tornado_angular import __version__
from tornado_angular.handlers import RequestHandler
from tornado_angular.handlers.angular_handler import (
    AngularIndexHandler,
    AngularRedirectHandler,
    AngularViewHandler,
    AngularConfigHandler
)
from tornado_angular.config import Config


def main():
    AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")
    TornadoAngularServer.run()


class VersionHandler(RequestHandler):
    def get(self):
        self.write(self.application.version)


class TornadoAngularServer(Server):
    def __init__(self, debug=None, *args, **kw):
        super(TornadoAngularServer, self).__init__(*args, **kw)
        self.force_debug = debug

    def get_extra_server_parameters(self):
        return {
            'no_keep_alive': False
        }

    def get_version(self):
        return __version__

    def get_settings(self):
        settings = super(TornadoAngularServer, self).get_settings()
        return settings

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

    def get_web_app_name(self):
        return "sandboxApp"

    def config_parser(self, parser):
        parser.add_argument('--version', action='store_true', default=False, help="Displays application's current version")

    def get_web_handlers(self):
        angular_path = abspath(self.config.ANGULAR_ROOT)

        items = (
            (r'bower_components', join(angular_path, 'bower_components')),
            (r'scripts', join(angular_path, '.tmp/scripts')),
            (r'styles', join(angular_path, '.tmp/styles')),
            (r'images', join(angular_path, 'app/images')),
        )

        handlers = []

        for url, path in items:
            handlers.append((
                r"/web/%s/(.+)" % url,
                tornado.web.StaticFileHandler,
                {'path': path}
            ))

        handlers.append((r'/web/views/(.+)', AngularViewHandler))
        handlers.append((r'/web/config.js', AngularConfigHandler))
        handlers.append((r'/web.+', AngularIndexHandler))

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

    def get_app(self):
        handlers = [
            ('/healthcheck/?', healthcheck.HealthCheckHandler),
        ]

        handlers = handlers + list(self.get_handlers())
        settings = self.get_settings()

        return tornado.web.Application(handlers, **settings)

    def get_config(self):
        return Config

    def get_web_allowed_config(self):
        return [
            'ANGULAR_ROOT',
            'FOO',
        ]

    def get_api_plugins(self):
        return []

    def get_plugins(self):
        return self.get_api_plugins()

    def api_after_start(self, io_loop):
        pass

    def after_start(self, io_loop):
        self.api_after_start(io_loop)
        self.application.allowed_configuration = self.get_web_allowed_config()
        self.application.web_app_name = self.get_web_app_name()
        self.application.version = self.get_version()

    def api_before_end(self, io_loop):
        pass

    def before_end(self, io_loop):
        self.api_before_end(io_loop)

    def start(self, args=None):
        options = self.parse_arguments(args)
        if options.version:
            print ("%s - version %s" % (self.get_server_name(), self.get_version()))
            sys.exit(0)

        super(TornadoAngularServer, self).start(args)

if __name__ == '__main__':
    main()
