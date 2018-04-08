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


