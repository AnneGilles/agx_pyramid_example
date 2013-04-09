# -*- coding: utf-8 -*-
import views
from pyramid.config import Configurator
from wsgiref.simple_server import make_server

def main():
    config = Configurator()
    config.add_static_view('static', 'static_resources/',)
    config.scan('views')
    config.scan()
    app = config.make_wsgi_app()
    return app

if __name__ == '__main__':
    app = main()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()