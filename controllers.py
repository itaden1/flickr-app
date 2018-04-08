from flickr_api import get_api
from views import get_template, render
from cgi import parse_qs

    
def controller(env):
    
    if env.get('REQUEST_METHOD') == 'GET':

        # get the template
        template = get_template()
   
        name = 'New York'
        lon = 73.935242
        lat = 40.730610

        # get raw json
        my_json = get_api(lon, lat)

        # convert json to html str
        html_images = json_to_html(my_json)

        return render(template, {'photos':html_images,'lon':lon,'lat':lat,'name':name})

    elif env.get('REQUEST_METHOD') == 'POST':

        # get template
        template = get_template()

        # get json data
        #my_json = get_api()
        try:
            r_body_size = int(env.get('CONTENT_LENGTH', 0))
        except (ValueError):
            r_body_size = 0
        d = env['wsgi.input'].read(r_body_size)
        data = parse_qs(d)
        lon = float(data.get(b'lon',[])[0])
        lat = float(data.get(b'lat',[])[0])
        name = str(data.get(b'location',[])[0])
        
        my_json = get_api(lon,lat)

        html_images = json_to_html(my_json)

        return render(template, {'photos':html_images,'lon':lon,'lat':lat,'name':name}) 

def json_to_html(json_obj):

    j = json_obj
    html_obj_list = []


    for p in j['photos']['photo']:

        img_src = 'https://farm{farm}.staticflickr.com/{server}/{p_id}_{secret}.jpg'.format(
                farm = p['farm'],
                server = p['server'],
                p_id = p['id'],
                secret = p['secret']
                )
        img_tag = '<div class="image"><img src="{}" alt="{}"/></div>'.format(img_src, p['title'])
        html_obj_list.append(img_tag)

    html = ''.join(html_obj_list)

    return html
