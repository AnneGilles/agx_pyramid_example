# -*- coding: utf-8 -*-
#from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='hello', renderer='templates/schas.pt')
def hello_world(request):
    #return Response('this is the stub for view hello_world')
    return {'foo': 'bar',  # return some variables for the schas template
            'project': 'pyramidonal',
            }
