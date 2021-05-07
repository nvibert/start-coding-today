import requests
import json

# Enable DEBUG mode for verbose output
DEBUG_MODE = True

# Generate a token in the Cloud Services Portal
REFRESH_TOKEN=''

# Cloud services portal URL
CSP_URL='https://console.cloud.vmware.com'
VMC_URL='https://vmc.vmware.com'

# The refresh token parameter 
# This is equivalent to the -d parameter that we pass into cURL: -d "refresh_token=$REFRESH_TOKEN"
# Except here in Python we are passing JSON because Python dictionaries make it super simple to work with JSON
params = {'refresh_token': REFRESH_TOKEN}
if DEBUG_MODE:
    print ('Params:\n',json.dumps(params))

# The request header 
# This is equivalent to the -H parameter we pass into cURL: -H "content-type: application/x-www-form-urlencoded"
# Here we're passing it JSON 
headers = {'Content-Type': 'application/json'}
if DEBUG_MODE:
    print ('Headers:\n',json.dumps(headers))

# Create the URL. You could build this directly in the requests.post
# We build it here to easily print it in debug mode
url = CSP_URL + '/csp/gateway/am/api/auth/api-tokens/authorize'
if DEBUG_MODE:
    print('Token Auth URL:',url)
    input('\n\nPress any key to continue')


# Execute the API request using the python Requests library
# This can look confusing if you're not used to Python syntax
# The first argument is a required positional argument - you can't call an API without sending a URL!
# The other two are called kwargs - or keyword arguments, the format of keyword=value
# We pass the keyword 'params' on the left the value in the variable params on the right
response = requests.post(url,params=params,headers=headers)
jsonResponse = response.json()
if DEBUG_MODE:
    print('\nRaw token JSON:\n',jsonResponse)
    print ('\nFormatted token JSON:\n',json.dumps(jsonResponse,indent=1),'\n\n')
    input('\n\nPress any key to continue')

# Extract the access_token from the JSON into a variable
access_token = jsonResponse['access_token']
if DEBUG_MODE:
    print('\nExtracted access token:', access_token)

# Build the URL to list organizations
url = VMC_URL + '/vmc/api/orgs'
if DEBUG_MODE:
    print('\nOrg list URL:',url)

# Build the headers for the GET request - we're using JSON, we pass the content type and the access token
org_list_headers =  {'Content-Type': 'application/json','csp-auth-token':access_token}
if DEBUG_MODE:
    print('\nOrg list headers: ', org_list_headers)
    input('\n\nPress any key to continue')

# Invoke the API - there are no parameters for this GET request, only headers
response = requests.get(url,headers=org_list_headers)

# Retrieve the JSON response
org_json = response.json()
if DEBUG_MODE:
    print('\nRaw Org JSON:', org_json)
    print('\nFormatted Org JSON',json.dumps(org_json,indent=2))
    # This code writes the JSON to a file for easier reading
    with open('orgs.json','w') as outfile:
        json.dump(org_json,outfile,indent=2)
    input('\n\nPress any key to continue')

# Print out the display_name for every org
print('Organization display names: ')
for org in org_json:
    print(org['display_name'])
