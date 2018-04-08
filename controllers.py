from flickr_api import get_api
from views import get_template, render
import models as db
from cgi import parse_qs

    
def controller(env):
    '''Main controller for the application'''
   
    
    if env.get('REQUEST_METHOD') == 'GET':

        # get the template
        template = get_template()
   
        # Default search location
        locations = db.get_locations()
        location_html = locations_to_html(locations)
        name = 'New York'
        lon = 73.935242
        lat = 40.730610

        # get raw json
        my_json = get_api(lon, lat)

        # convert json to html str
        html_images = json_to_html(my_json)

        return render(template, {'photos':html_images,'lon':lon,'lat':lat,'name':name,'options':location_html})

    elif env.get('REQUEST_METHOD') == 'POST':
        
        # get POST Data
        try:
            r_body_size = int(env.get('CONTENT_LENGTH', 0))
        except (ValueError):
            r_body_size = 0


        # get template
        template = get_template()
        
        d = env['wsgi.input'].read(r_body_size)
        data = parse_qs(d)
        lon = float(data.get(b'lon',[])[0])
        lat = float(data.get(b'lat',[])[0])
        try:
            name = (data.get(b'location-name',[])[0]).decode('utf-8')
        except:
            name = 'Mystery location'

        if b'pre-location-search' in data:
            loc_id = int(data.get(b'location-select',[])[0])
            print(loc_id)
            loc = db.get_location(loc_id)
            print(loc)
            name = loc[0][1]
            lon = loc[0][2]
            lat = loc[0][3]

        if b'location-save' in data:
            db.save_location(name, lon, lat)


        locations = db.get_locations()
        location_html = locations_to_html(locations)
        # get json data
        my_json = get_api(lon,lat)

        html_images = json_to_html(my_json)

        return render(template, {'photos':html_images,'lon':lon,'lat':lat,'name':name,'options':location_html}) 

def json_to_html(json_obj):
    '''Used to convert JSON data returned by the flickr api into html'''

    j = json_obj
    html_obj_list = []


    # for each photo in SJON object create a div and image tag
    for p in j['photos']['photo']:
        
        #construct url for img src atribute
        img_src = 'https://farm{farm}.staticflickr.com/{server}/{p_id}_{secret}.jpg'.format(
                farm = p['farm'],
                server = p['server'],
                p_id = p['id'],
                secret = p['secret']
                )
        #construct the img element
        img_tag = '<div class="image"><img src="{}" alt="{}"/></div>'.format(img_src, p['title'])
        html_obj_list.append(img_tag)

    html = ''.join(html_obj_list)

    return html

def locations_to_html(locations):
    
    html_list = []
    for l in locations:
        html = '<option value="{}">{}</option>'.format(l[0],l[1])
        html_list.append(html)

    html = ''.join(html_list)
    return html


