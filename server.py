from http.server import BaseHTTPRequestHandler, HTTPServer
import os

from my_controller import controller




class AppHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        rootdir = os.path.dirname(os.path.realpath(__file__))
        try:
            if self.path.endswith('/'):
                content = controller()
                
                self.send_response(200)

                self.send_header('Content-type', 'text/html')
                self.end_headers()

                self.wfile.write(content)
                return

        except IOError:
            self.send_error(404, 'file not found')


def run():
    print ('HTTP Server is starting...')

    server_address = ('127.0.0.1', 8080)
    httpd = HTTPServer(server_address, AppHTTPRequestHandler)

    print ('HTTP Server is running...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
