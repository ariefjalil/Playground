import requests, re, time, base64, urllib
from requests_oauthlib import OAuth1


ConsumerKey    = 'OwnAccount'
ConsumerSecret = 'OwnAccount'

TokenKey       = '+aMfAePU2zrcTh8wRrS-qERs4bftUQ'
TokenSecret    = 'WFXzfstkQz@B87cU3G2d7wNxf7AVfv4+CcuFqgs-'
tenant         = 'c6210ea0-c7a5-4163-b6a8-e256015714ae'

fileContent = ' '
headers={}
headers['Accept']					= 'application/json'
headers['Accept']					= 'text/xml'
headers['X-Tradeshift-TenantId']	= 'tenant'
headers['Content-Type']				='text/xml'

def get(url):
	auth = OAuth1(ConsumerKey, ConsumerSecret, TokenKey, TokenSecret)
	response = requests.get(url, headers=headers, auth=auth)
	return response.content
	#return response.status_code			

def delete(url):
	auth = OAuth1(ConsumerKey, ConsumerSecret, TokenKey, TokenSecret)
	response = requests.delete(url, headers=headers, auth=auth)
	return response.status_code

def post(url):
	auth = OAuth1(ConsumerKey, ConsumerSecret, TokenKey, TokenSecret)
	response = requests.post(url, headers=headers, auth=auth, data=fileContent)
	#return response.content
	return response.status_code
	print response.content
	

def put(url):
	auth = OAuth1(ConsumerKey, ConsumerSecret, TokenKey, TokenSecret)
	response = requests.put(url, headers=headers, auth=auth, data=fileContent)
	print response.status_code
	print response.content
	


url ='https://api.tradeshift.com/tradeshift/rest/external/account/branches/c6210ea0-c7a5-4163-b6a8-e256015714ae'
print get (url)
