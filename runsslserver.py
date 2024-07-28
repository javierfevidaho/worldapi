import os
import ssl
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application
from wsgiref.simple_server import make_server, WSGIRequestHandler, WSGIServer

class SSLWSGIServer(WSGIServer):
    def __init__(self, server_address, HandlerClass, bind_and_activate=True):
        super().__init__(server_address, HandlerClass, bind_and_activate)
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')
        self.socket = context.wrap_socket(self.socket, server_side=True)

class SSLWSGIRequestHandler(WSGIRequestHandler):
    def make_environ(self):
        environ = super().make_environ()
        environ['wsgi.url_scheme'] = 'https'
        return environ

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'worldapi.settings')
    application = get_wsgi_application()

    server_address = ('127.0.0.1', 8000)
    httpd = make_server(
        server_address[0],
        server_address[1],
        application,
        server_class=SSLWSGIServer,
        handler_class=SSLWSGIRequestHandler,
    )

    print(f'Starting HTTPS server at https://{server_address[0]}:{server_address[1]}')
    httpd.serve_forever()
