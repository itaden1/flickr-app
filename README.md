# flickr-app
An attempt at creating a Python web application with no Frameworks or third party tools.
Undertaken as a learning experience.

## Instructions
*Requires Python3.5 or greater. No additional modules required*
* Download or clone this repo
* Fire up a python interpreter and enter the following to initiate the database
```Python
>>>from models import create_tables
>>>create_tables()
>>>exit()
```
* Start the server by entering the following at the command prompt
```
$python3 wsgi_server.py
```
* open up your browser and navigate to **localhost:8000**

## To Do
* Form validation to prevent double entries in database
* Navigation for getting the next ten search results

