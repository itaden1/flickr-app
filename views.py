import os

def get_template():
    '''Open the html template file and return it as a string''' 
    with open('index.html', 'r') as template:
        html = template.read()
    return html

def render(template, args={}):
    '''Render the template with variable data'''

    photos = args['photos']
    if len(photos) == 0:
        photos = '<p>no photos found for this location</p>'
    
    # unpack variables from dictionary
    lon = str(args['lon'])
    lat = str(args['lat'])
    name = (args['name'])
    options = (args['options'])
    
    # render variables using string.replace
    html = template.replace('$photos', photos)
    html = html.replace('$options', options)
    html = html.replace('$location', name)
    html = html.replace('$lon', lon)
    html = html.replace('$lat', lat)
    return html
    
