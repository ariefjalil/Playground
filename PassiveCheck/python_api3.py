import requests, re, time, base64, urllib
from requests_oauthlib import OAuth1


ConsumerKey    = 'OwnAccount'
ConsumerSecret = 'OwnAccount'

TokenKey       = 'Shmxjw79YeUYyqcUSkFDZmsQN2bA3M'
TokenSecret    = 'BDyT7-mhKT92NCUeGdryqX5cgX4B6kTaaA2ZF4gY'
tenant         = 'ff93a5eb-75f0-49c2-8c4c-6bce9b81f970'

fileContent = ' '
#headers={}

headers = {'Accept' : 'application/json','X-Tradeshift-TenantId' :tenant,'Content-Type' : 'text/xml'}

'''
headers['Accept']             = 'application/json' 
headers['Accept']             = 'text/xml'
headers['X-Tradeshift-TenantId'] = 'tenant'
headers['Content-Type']          ='text/xml'

'''

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
   print("response.content")
   return response.status_code
   
   

def put(url):
   auth = OAuth1(ConsumerKey, ConsumerSecret, TokenKey, TokenSecret)
   response = requests.put(url, headers=headers, auth=auth, data=fileContent)
   print("response.status_code")
   print("response.content")
   


url ='https://api.tradeshift.com/tradeshift/rest/external/account/branches/c6210ea0-c7a5-4163-b6a8-e256015714ae'
print (get(url))
