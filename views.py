import os

def get_template():
    
    with open('index.html', 'r') as template:
        html = template.read()
    return html

def render(template, args={}):
    var = args['name']
    return template.replace('{{}}', var)
    
