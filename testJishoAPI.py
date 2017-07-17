# Python file for testing jisho.org's API

# link to their API, note that their API is also a work in progress
# http://jisho.org/api/v1/search/words?keyword=amazing

url = "http://jisho.org/api/v1/search/words?keyword=amazing"

import json
import requests

r = requests.get(url)
print (r.json())

