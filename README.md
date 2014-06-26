tornado-angular [![Build Status](https://travis-ci.org/heynemann/tornado-angular.svg?branch=master)](https://travis-ci.org/heynemann/tornado-angular)
=====================================================================================================================================================

tornado-angular is an opinionated way of distributing angular applications with tornado web server as api handler.

Creating a new app
------------------

The expected directory structure for tornado-angular is as follows:

```
    my_app_name
    ├── setup.py
    ├── other files(Makefile, Procfile, travis, etc)
    ├── my_app_name
    │   ├── config
    │   │   ├── __init__.py
    │   │   ├── local.conf
    │   │   ├── testing.conf
    │   │   └── prod.conf
    │   ├── api
    │   │   └── handlers
    │   │       ├── api_handler_1.py
    │   │       ├── api_handler_2.py
    │   │       └── __init__.py
    │   ├── __init__.py
    │   ├── server.py
    │   ├── version.py
    │   └── web
    │       ├── app
    │       │   ├── images
    │       │   │   └── yeoman.png
    │       │   ├── index.html
    │       │   ├── robots.txt
    │       │   ├── scripts
    │       │   │   ├── app.coffee
    │       │   │   ├── controllers
    │       │   │   │   ├── main.coffee
    │       │   │   │   └── about.coffee
    │       │   │   ├── directives
    │       │   │   │   ├── login.coffee
    │       │   │   │   └── header.coffee
    │       │   │   └── services
    │       │   │       ├── api.coffee
    │       │   │       └── google.coffee
    │       │   ├── styles
    │       │   │   └── main.scss
    │       │   └── views
    │       │       ├── about.html
    │       │       └── main.html
    │       ├── bower_components
    │       │   └── auto-creted by bower
    │       ├── bower.json
    │       ├── Gruntfile.js
    │       ├── package.json
    │       └── test
    │           ├── karma.conf.coffee
    │           └── spec
    │               ├── controllers
    │               ├── directives
    │               └── services
    └─── tests
         ├── __init__.py
         └── test_something.py
```
