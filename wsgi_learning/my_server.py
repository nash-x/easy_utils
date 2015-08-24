from paste import httpserver
from paste.deploy import loadapp

if __name__ == '__main__':
    app = loadapp('config:api-paste.ini', relative_to='.')
    httpserver.serve(app, host='127.0.0.1', port='8081')