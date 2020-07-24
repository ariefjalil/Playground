# -*- coding: utf-8 -*-
import time, uuid, datetime
import requests, json
from requests_oauthlib import OAuth1

ConsumerKey    = 'OwnAccount'
ConsumerSecret = 'OwnAccount'
home_folder = '/Users/screwed/Desktop/Python/Branches/'

TokenKey       = 'XnRdPNWgFspFqV35JeKzKpymQmQpwn'
TokenSecret    = 'nXguYjnfe7ch3-MfUdPg4gZ29cathHGPD8YnTGWV'
tenant         = 'c8a187c2-c129-4536-9e99-90d6fc33aeb2'


fileContent=''

headers        = {'Accept' : 'application/json',
                'X-Tradeshift-TenantId' : tenant,
                'Content-Type' : 'application/json'}
def get(url):
    auth = OAuth1(ConsumerKey, ConsumerSecret, TokenKey, TokenSecret)
    response = requests.get(url, headers=headers, auth=auth)
    # return response.content
    # return response.status_code
    return response
def delete(url):
    auth = OAuth1(ConsumerKey, ConsumerSecret, TokenKey, TokenSecret)
    response = requests.delete(url, headers=headers, auth=auth)
    return response
def post(url):
    auth = OAuth1(ConsumerKey, ConsumerSecret, TokenKey, TokenSecret)
    response = requests.post(url, headers=headers, auth=auth, data=fileContent)
    return response
def put(url):
    auth = OAuth1(ConsumerKey, ConsumerSecret, TokenKey, TokenSecret)
    response = requests.put(url, headers=headers, auth=auth, data=fileContent)
    return response

# randomizer= str(uuid.uuid4())

content = open(home_folder + 'ajx_wipro_SMD.csv').readlines()

logname=str(datetime.datetime.now())[:10]
logFile = open(home_folder + logname+'.csv', 'a+')

ApiAcessTokenList = open(home_folder + 'ajx_wiproAPI.csv').readlines()

dictTokenKey={}
dictTokenSecret={}
for i in ApiAcessTokenList:
    if i.split(';')[0].strip()!='tenantid':
        dictTokenKey[i.split(';')[0]]   =i.split(';')[2].strip()
        dictTokenSecret[i.split(';')[0]]=i.split(';')[1].strip()

for i in dictTokenKey:
    print(i, dictTokenKey[i], dictTokenSecret[i], 'OwnAccount')


count = 0
print('STARTING---------------------------------------------\n\n')
for i in content:
    if i.split(';')[0].strip()!='EmailMaster':
        ParentCompanyAccountId  = i.split(';')[1].strip()   #OK
        companyEmail            = i.split(';')[3].strip()   #OK
        companyName             = i.split(';')[2].strip()   #OK
        companyCountry          = i.split(';')[4].strip()   #OK
        companyPassword         = i.split(';')[9].strip()   #OK

        branchScheme1           = i.split(';')[5].strip()   #OK
        branchId1               = i.split(';')[6].strip()   #OK
        branchScheme2           = i.split(';')[7].strip()   #OK
        branchId2               = i.split(';')[8].strip()   #OK

        companyId               = str(uuid.uuid4())
        companyEmailId          = str(uuid.uuid4())
        count +=1
        TokenKey = dictTokenKey[ParentCompanyAccountId]
        TokenSecret = dictTokenSecret[ParentCompanyAccountId]
        tenant = ParentCompanyAccountId
        headers = {'Accept' : 'application/json','X-Tradeshift-TenantId' : tenant,'Content-Type' : 'application/json'}
        data = {"Activate": "true","CompanyAccount":{"Company": {"CompanyName": "companyNameHere","Country": "companyCountryHere","Identifier" : [{"scheme": "scheme1Here", "value": "value1Here"},{"scheme": "scheme2Here", "value": "value2Here"}]},"Id": "companyIdHere","State": "CREATED"},"ParentCompanyAccountId": "ParentCompanyAccountIdHere","SendActivationEmail": "false","User": {"CompanyAccountId": "companyIdHere","Credentials": [{"CredentialType": "UsernamePasswordCredential","Password": "companyPasswordHere","Username": "companyEmailHere"}],"Id": "companyEmailIdHere","Kind": "PERSON","Person": {"Email": "companyEmailHere","FirstName": "","LastName": "","Title": ""},"State": "CREATED","TimeZone": "UTC","UserName": "companyEmailHere"}}
        json_dump = json.dumps(data)
        json_object = json.loads(json_dump)
        json_object["CompanyAccount"]["Company"]["CompanyName"] = companyName
        json_object["CompanyAccount"]["Company"]["Country"]     = companyCountry
        json_object["CompanyAccount"]["Id"]                     = companyId
        json_object["ParentCompanyAccountId"]                   = ParentCompanyAccountId
        json_object["User"]["CompanyAccountId"]                 = companyId
        json_object["User"]["Credentials"][0]["Username"]       = companyEmail
        json_object["User"]["Credentials"][0]["Password"]       = companyPassword
        json_object["User"]["Id"]                               = companyEmailId
        json_object["User"]["Person"]["Email"]                  = companyEmail
        json_object["User"]["UserName"]                         = companyEmail
        json_object["CompanyAccount"]["Company"]["Identifier"]  = []
        if len(branchScheme1)>0 and len(branchId1)>0:
            json_object["CompanyAccount"]["Company"]["Identifier"]  += [{"scheme": branchScheme1, "value": branchId1}]
        if len(branchScheme2)>0 and len(branchId2)>0:
            json_object["CompanyAccount"]["Company"]["Identifier"]  += [{"scheme": branchScheme2, "value": branchId2}]
        json_dump = json.dumps(json_object)
        url = 'https://api.tradeshift.com/tradeshift/rest/external/account/branches/new'
        fileContent = json_dump
        create = put(url)
        logFile = open(logname+'.csv', 'a+')
        errorMessage = ''
        if create.status_code != 204:
            errorMessage = ';'+str(create.content.decode('utf-8'))
        if create.status_code == 204:
            url = 'https://api.tradeshift.com/tradeshift/rest/external/account/info'
            headers['X-Tradeshift-TenantId'] = companyId
            autoAcceptProfile = get(url).content.decode('utf-8').replace('"AutoAcceptConnections" : false,', '"AutoAcceptConnections" : true,')
            fileContent = autoAcceptProfile
            autoAccept = put(url)
            if autoAccept.status_code != 204:
                errorMessage = ';'+str(autoAccept.content.decode('utf-8'))
            if autoAccept.status_code == 204:
                errorMessage = ';;AutoAcceptConnections set to True'
        toWrite =  ParentCompanyAccountId+';'+companyEmail+';'+companyName+';'+companyCountry+';'+companyPassword+';'+companyId+';'+companyEmailId+';'+str(create.status_code)+';'+str(count)+errorMessage
        logFile.write(toWrite)
        logFile.write('\n')
        logFile.close()
        print(create.status_code,ParentCompanyAccountId, companyEmail, companyName, companyCountry, companyPassword, companyId, companyEmailId, count)
        time.sleep(1)

print('\n\n\t\tDONE.\n\n')
