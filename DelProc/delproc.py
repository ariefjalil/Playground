import requests, re, time, base64, urllib
from requests_oauthlib import OAuth1

ConsumerKey    = 'OwnAccount'
ConsumerSecret = 'OwnAccount'

TokenKey       = '8NUYNv+QMcj9X@8zEKpc76bbDutWW5'
TokenSecret    = 'Kdv39udqUMZxpY+qQ-GtD-ZRuVAtFfXRvEg2t@kx'
tenant         = 'cb65aa12-9edb-428b-a251-c40f62c3c9e7'

headers        = {'Accept' : 'application/json',
				'X-Tradeshift-TenantId' : tenant,
				'Content-Type' : 'text/xml'}

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
	print response.content
	return response.status_code
def put(url):
	auth = OAuth1(ConsumerKey, ConsumerSecret, TokenKey, TokenSecret)
	response = requests.put(url, headers=headers, auth=auth, data=fileContent)
	print response.content
	print response.status_code
def deleteAll():
	stuck = ''
	count = 0
	pageLimit = 0
	currentPage = 0
	url = 'https://api-sandbox.tradeshift.com/tradeshift/rest/external/documentfiles?directory=processing&limit=100&page='+str(pageLimit)
	for i in re.findall(r'"numPages" : (.*?),', get('https://api.tradeshift.com/tradeshift/rest/external/documentfiles?directory=processing&limit=100&page=0')):
		pageLimit = int(i)-1
	while currentPage <= pageLimit:
		url = 'https://api-sandbox.tradeshift.com/tradeshift/rest/external/documentfiles?directory=processing&limit=100&page='+str(currentPage)
		stuck += str(get(url))
		currentPage +=1
	howMany = len(re.findall(r'"FileName" : "(.*?)",', stuck))
	for i in re.findall(r'"FileName" : "(.*?)",', stuck):
		url = 'https://api-sandbox.tradeshift.com/tradeshift/rest/external/documentfiles/'+str(i)+'/file?directory=processing'
		count +=1
		if delete(url) == 204:
			print str(count)+'/'+str(howMany), i
		else:
			print i, 'deleting failed'
def deleteOne(fileName):
	url = 'https://api-sandbox.tradeshift.com/tradeshift/rest/external/documentfiles/'+str(fileName)+'/file?directory=processing'
	if delete(url) == 204:
		print 'Deleting', fileName, 'was successful.'
	else:
		print 'Deleting', fileName, 'failed.'



#deleteOne('invoice899.xml')
deleteAll()


