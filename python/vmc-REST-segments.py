### List segments in VMC ###
import requests
import json

# Enable DEBUG mode for verbose output
DEBUG_MODE = True

# Generate a token in the Cloud Services Portal
REFRESH_TOKEN=''

# Cloud services portal
CSP_URL='https://console.cloud.vmware.com'
VMC_URL='https://vmc.vmware.com'

params = {'refresh_token': REFRESH_TOKEN} 
headers = {'Content-Type': 'application/json'}
url = CSP_URL + '/csp/gateway/am/api/auth/api-tokens/authorize'
response = requests.post(url,params=params,headers=headers)
jsonResponse = response.json()
access_token = jsonResponse['access_token']

# Build the URL to list segments
url = 'https://nsx-xx-xx-xx-xxx.rp.vmwarevmc.com/vmc/reverse-proxy/api/orgs/xx/sddcs/xx/policy/api/v1/infra/tier-1s/cgw/segments'
if DEBUG_MODE:
    print('\nSegment list URL:',url)

# Build the headers for the GET request - we're using JSON, we pass the content type and the access token
seg_list_headers =  {'Content-Type': 'application/json','csp-auth-token':access_token}

# Invoke the API - there are no parameters for this GET request, only headers
response = requests.get(url,headers=seg_list_headers)

# Retrieve the JSON response
seg_json = response.json()
if DEBUG_MODE:
    print('\nRaw Seg JSON:', seg_json)
    print('\nFormatted Seg JSON',json.dumps(seg_json,indent=2))
    # This code writes the JSON to a file for easier reading
    with open('seg.json','w') as outfile:
        json.dump(seg_json,outfile,indent=2)

# Print out segment details

