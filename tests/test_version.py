#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of tornado_angular.
# https://github.com/heynemann/tornado-angular

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Bernardo Heynemann heynemann@gmail.com

from preggy import expect

from tornado_angular import __version__
from tests.base import TestCase


class VersionTestCase(TestCase):
    def test_has_proper_version(self):
        expect(__version__).to_equal("0.1.0")
