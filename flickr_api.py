import urllib.request
import json


def get_api(lon, lat): 
    '''Connect to the twitter API to return JSON'''

    api_key = '21b02096b58b0fedf2e3b59fc9c052a1'
    secret = 'c2f288491426499a'

    page = 1

    format_type = 'json'
    
    # construct api request url
    url = 'https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key={}&secret={}&lat={}&lon={}&format={}&page={}&per_page=10'.format(
            api_key,
            secret,
            lat,
            lon,
            format_type,
            page,
            )

    # send the request
    jsonp_response = urllib.request.urlopen(url).read()
    
    # strip the function call from the front of the JSON string
    my_json = jsonp_response[len('jsonFlickrApi('):-1]

    # create a python readable dict from JSON string
    response = json.loads(my_json.decode('utf-8'))

    return response
