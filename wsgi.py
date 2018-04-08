import controllers


def application(environ, start_response):
    '''Main application for interfacing with WSGI'''

    if environ.get('PATH_INFO') == '/':
        status = '200 OK'
        content = controllers.controller(environ)
    else:
        status = '404 NOT FOUND'
        content = 'page not found'

    response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(content)))]
    start_response(status, response_headers)
    
    return [content.encode('utf-8')]


# Basic WSGI server for testing purposes

if __name__ == '__main__':
    from wsgiref import simple_server
    server = simple_server.make_server('', 8000, application)
    
    print('Server running at 127.0.0.1:8000')
    server.serve_forever()


