from main import application
# Basic WSGI server for testing purposes

if __name__ == '__main__':
    from wsgiref import simple_server
    server = simple_server.make_server('', 8000, application)
    
    print('Server running at 127.0.0.1:8000')
    server.serve_forever()


