# -*- coding: utf-8 -*-
#import views
from pyramid.config import Configurator
#from wsgiref.simple_server import make_server


def main(global_config, **settings):
    config = Configurator()
    config.add_static_view('static', 'static_resources/',)
    #config.scan(".views")  # already performed by config.scan()
    config.add_route('hello', '/')
    config.scan()
    app = config.make_wsgi_app()
    return app

#if __name__ == '__main__':
#    app = main()
#    server = make_server('0.0.0.0', 8080, app)
#    server.serve_forever()
