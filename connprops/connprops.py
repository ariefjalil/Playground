
# -*- coding: utf-8 -*-
import requests, re, time, base64, urllib
from requests_oauthlib import OAuth1

ConsumerKey    = 'OwnAccount'
ConsumerSecret = 'OwnAccount'

#CUSTOMER MASTER - API CREDENTIALS
TokenKey       = 'Token'
TokenSecret    = 'TokenSecret'
tenant         = 'Tenant UUID'

fileContent=''

headers        = {'Accept' : 'application/json',
				'X-Tradeshift-TenantId' : tenant,
				'Content-Type' : 'text/xml'}
def get(url):
	auth = OAuth1(ConsumerKey, ConsumerSecret, TokenKey, TokenSecret)
	response = requests.get(url, headers=headers, auth=auth)
	#print response.status_code,
	return response.content
def delete(url):
	auth = OAuth1(ConsumerKey, ConsumerSecret, TokenKey, TokenSecret)
	response = requests.delete(url, headers=headers, auth=auth)
	return response.status_code
def post(url):
	auth = OAuth1(ConsumerKey, ConsumerSecret, TokenKey, TokenSecret)
	response = requests.post(url, headers=headers, auth=auth, data=fileContent)
	return response.content
	#print response.content
	#print response.status_code
def put(url):
	auth = OAuth1(ConsumerKey, ConsumerSecret, TokenKey, TokenSecret)
	response = requests.put(url, headers=headers, auth=auth, data=fileContent)
	print response.status_code
	return response.content


dict2={}

x = get('https://api-sandbox.tradeshift.com/tradeshift/rest/external/account/branches')
for i in re.findall(r'(?s)CompanyName.*?AccountType', x):
	for j in re.findall(r' "scheme" : "CustomerAssignedId",\n *?"value" : "(.*?)"', i):
		branch = j
	for j in re.findall(r'"CompanyAccountId" : "(.*?)",', i):
		branchTenant =  j
		dict2[branch] = branchTenant

file = open('/Users/ovidiupavel/Documents/Python/Standalone Account/SMD_Supplier OPA.csv').readlines()

count = 0
for k in file:
	SBS_INACTIVE = k.split(';')[0]
	branch = k.split(';')[1]
	AccountingSystemId = k.split(';')[2]
	SupplierCategory = k.split(';')[3]
	INVOICE_CURRENCY_CODE = k.split(';')[4]	
	PAY_SITE_FLAG = k.split(';')[5]
	PURCHASING_SITE_FLAG = k.split(';')[6].strip()
	if count > 0:
		if branch in dict2:
			headers= {'Accept' : 'text/xml','X-Tradeshift-TenantId' : dict2[branch],'Content-Type' : 'text/xml'}
			url = 'https://api-sandbox.tradeshift.com/tradeshift/rest/external/network/connect/'+'1706fa8d-6c09-48f1-844b-9e8ce0b3a558'
			fileContent=''
			connection=post(url)
			url = 'https://api-sandbox.tradeshift.com/tradeshift/rest/external/network/connections/companies/'+'1706fa8d-6c09-48f1-844b-9e8ce0b3a558'
			connection = get(url)
			for i in re.findall(r'<ts:ConnectionId>(.*?)</ts:ConnectionId>', connection):
				connectionid = i
			url = 'https://api-sandbox.tradeshift.com/tradeshift/rest/external/network/connections/'+connectionid+'/properties'
			headers['Content-Type']='application/json'
			fileContent='''{
	"Items": [
		{
			"Key": "SBS_INACTIVE",
			"Values": [
				"'''+SBS_INACTIVE+'''"
			]
		},
		{
			"Key": "branch",
			"Values": [
				"'''+branch+'''"
			]
		},
		{
			"Key": "AccountingSystemId",
			"Values": [
				"'''+AccountingSystemId+'''"
			]
		},
		{
			"Key": "SupplierCategory",
			"Values": [
				"'''+SupplierCategory+'''"
			]
		},
		{
			"Key": "INVOICE_CURRENCY_CODE",
			"Values": [
				"'''+INVOICE_CURRENCY_CODE+'''"
			]
		},
		{
			"Key": "PAY_SITE_FLAG",
			"Values": [
				"'''+PAY_SITE_FLAG+'''"
			]
		},
		{
			"Key": "PURCHASING_SITE_FLAG",
			"Values": [
				"'''+PURCHASING_SITE_FLAG+'''"
			]
		}
	]
}'''
			#print fileContent
			print put(url)
			
	
		else:
			print branch, 'not found'
	count +=1
	print str(count)+'/'+str(len(file))
	time.sleep(5)
SMD_Supplier OPA.py
Displaying SMD_Supplier OPA.py.