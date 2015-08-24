import webob
from webob import dec
class Request(webob.Request):
    pass

class Configured:
    def __init__(self, name, greeting):
        self.name = name
        self.greeting = greeting

    def __call__(self, environ, start_response):
        status = '200 OK'
        response_headers = [('Content-Type', 'text/plain')]
        start_response(status, response_headers)
        return ['%s, %s!\n' % (self.greeting, self.name)]


class WSGIConfigured:
    def __init__(self, name, greeting):
        self.name = name
        self.greeting = greeting

    @dec.wsgify(RequestClass=Request)
    def __call__(self, *args, **kwargs):

        return webob.Response('hey there, name: %s, greeting: %s' % (self.name, self.greeting))


def app_factory(global_config, name='Ivy', greeting='Shuang'):
    return WSGIConfigured(name, greeting)

def new_app_factory(global_config, name='Johnny', greeting='Howdy'):
    return WSGIConfigured(name, greeting)