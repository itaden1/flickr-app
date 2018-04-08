import os

def get_template():
    
    with open('index.html', 'r') as template:
        html = template.read()
    return html

def render(template, args={}):
    photos = args['photos']
    if len(photos) == 0:
        photos = '<p>no photos found for this location</p>'
    lon = str(args['lon'])
    lat = str(args['lat'])
    name = str(args['name'])
    html = template.replace('$photos', photos)
    html = html.replace('$location', name)
    html = html.replace('$lon', lon)
    html = html.replace('$lat', lat)
    return html
    
