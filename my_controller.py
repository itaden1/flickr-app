from flickr_api import get_api
from views import get_template, render

    
def controller():
    
    # get the template
    template = get_template()
    
    # get raw json
    my_json = get_api()
    
    # convert json to html str
    html = json_to_html(my_json)

    return render(template, {'name':html}).encode()

def json_to_html(json_obj):

    j = json_obj
    html_obj_list = []


    for p in j['photos']['photo']:

        img_src = 'https://farm{farm}.staticflickr.com/{server}/{p_id}_{secret}_o.(jpg|gif|png)'.format(
                farm = p['farm'],
                server = p['server'],
                p_id = p['id'],
                secret = p['secret']
                )
        img_tag = '<img src="{}" alt="{}"/>'.format(img_src, p['title'])
        html_obj_list.append(img_tag)

    html = ''.join(html_obj_list)

    return html
