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

Creating a server
-----------------

Just inherit from `tornado_angular.server` and override the methods that you need to change.

```python
class MyShinyAppServer(Server):
    def get_api_handlers(self):
        return [
            ('do-something/?', MyShinyHandler),  # actually gets mapped to /api/do-something/?
        ]

    def get_api_prefix(self):
        return "api"

    def get_web_app_name(self):
        return "my-shiny-app"

    # things listed here will go from your config file to the ConfigConst module in angular
    # to include the ConfigConst module just add to your index.html:
    # <script src="{{ static_url('config.js') }}"></script>
    def get_web_allowed_config(self):
        return [
            'BAZ',
            'FOO',
            'BAR',
        ]

    # cow framework plug-ins that your api requires
    def get_api_plugins(self):
        return []

    # any initialization you need to perform after the server is up
    def api_after_start(self, io_loop):
        pass

    # any destruction you need to perform before the server goes down
    def api_before_end(self, io_loop):
        pass

def main():
    MyShinyAppServer.run()

if __name__ == '__main__':
    main()
```

How do I run my angular/tornado app?
------------------------------------

In your setup.py file, include the following:

```python
    entry_points={
        'console_scripts': [
            'my_shiny_app=my_shiny_app.server:main',
        ],
    },
```

Now in order to run your app, all you have to do is install it and run the `my_shiny_app` command, like this:

```bash
$ pip install -e .
$ my_shiny_app -vvv -d -c ./my_shiny_app/config/local.conf -p 8000

2014-06-25 19:07:43,851 - root - INFO - Loading configuration file at /home/user/my-shiny-app/my_shiny_app/config/local.conf...
2014-06-25 19:07:43,851 - root - INFO - Using configuration file at /home/user/my-shiny-app/my_shiny_app/config/local.conf.
2014-06-25 19:07:43,852 - root - INFO - -- Server started listening in 0.0.0.0:8000 --
```
