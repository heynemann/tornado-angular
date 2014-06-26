#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of tornado_angular.
# https://github.com/heynemann/tornado-angular

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Bernardo Heynemann heynemann@gmail.com

try:
    from ujson import loads, dumps
except ImportError:
    from json import loads, dumps