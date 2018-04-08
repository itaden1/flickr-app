import urllib.request
import json


def get_api(lon=73.935242, lat=40.730610): 
    
    print (lon)

    api_key = '21b02096b58b0fedf2e3b59fc9c052a1'
    secret = 'c2f288491426499a'

    page = 1

    format_type = 'json'

    url = 'https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key={}&secret={}&lat={}&lon={}&format={}&page={}&per_page=10'.format(
            api_key,
            secret,
            lat,
            lon,
            format_type,
            page,
            )

    jsonp_response = urllib.request.urlopen(url).read()

    my_json = jsonp_response[len('jsonFlickrApi('):-1]

    response = json.loads(my_json.decode('utf-8'))

    return response
