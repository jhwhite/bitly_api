import requests
import json

url_to_shorten = raw_input('What is the URL you wish to bitly?\n')
query_params = {'access_token': 'b6e72c0669c9829131cbd85125bd4b35ba54e6ce',
                'longUrl': url_to_shorten} 

endpoint = 'https://api-ssl.bitly.com/v3/shorten'
response = requests.get(endpoint, params= query_params)

data = json.loads(response.content)
print data['data']['url']

