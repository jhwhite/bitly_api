import requests
import json
from sys import argv

script, filename = argv

text = open(filename)

for line in text.readlines():
#url_to_shorten = raw_input('What is the URL you wish to bitly?\n')
	query_params = {'access_token': '',
	                'longUrl': line} 

	endpoint = 'https://api-ssl.bitly.com/v3/shorten'
	response = requests.get(endpoint, params= query_params)

	data = json.loads(response.content)
	#print data['data']['url']

text.close()
