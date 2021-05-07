import requests
import json

# Environment variables
VC_USERNAME = ''
VC_PASSWORD = ''
VC_URL = ''

# Prints out debugging information if set to true
DEBUG_MODE = True

# API header to use for the session token
SESSION_HEADER = {"Content-Type": "application/json","Accept": "application/json"}

# Build the API URL to retrieve a session token
vc_session_url = VC_URL + '/rest/com/vmware/cis/session'
if DEBUG_MODE:
    print('Session token URL:',vc_session_url)

# Invoke the API to retrieve a session token
response = requests.post(vc_session_url,headers=SESSION_HEADER,auth=(VC_USERNAME,VC_PASSWORD),verify=False)
if DEBUG_MODE:
    print ('Session response status: ', response.status_code)

# Save the JSON sent back by the API into a variable
session_json = response.json()
if DEBUG_MODE:
    print('Session JSON: ',session_json)

# Extract the session token from the response JSON
session_token = session_json['value']
if DEBUG_MODE:
    print('Session token: ', session_token)

folder_filter_spec = {"type","VIRTUAL_MACHINE"}

# Header for the list folders API call, passing it the session token that we retrieved earlier
GET_HEADER = {"Content-Type": "application/json","Accept": "application/json","vmware-api-session-id":session_token}
if DEBUG_MODE:
    print('GET_HEADER: ',GET_HEADER)

# Build the API URL to list folders
vc_folder_url = VC_URL + '/rest/vcenter/folder'
if DEBUG_MODE:
    print('FOLDER URL:', vc_folder_url)

# Invoke the API to list folders
response = requests.get(vc_folder_url,headers=GET_HEADER,verify=False)
if DEBUG_MODE:
    print ('Folder response status: ', response.status_code)

# Save the JSON sent back by the API into a variable
folder_json = response.json()
if DEBUG_MODE:
    print ('Raw folder JSON:\n',folder_json)
    print ('Formatted folder JSON:\n',json.dumps(folder_json,indent=1),'\n\n')

# Print the folder list
print('All folders found on vCenter',VC_URL)
for fldr in folder_json['value']:
    print(fldr['name'], '(',fldr['type'],')')

# Print only VM folders
print('\n\nVM folders found on vCenter',VC_URL)
for fldr in folder_json['value']:
    if fldr['type'] == 'VIRTUAL_MACHINE':
        print(fldr['name'], '(',fldr['type'],')')

# Now write the next set of code yourself using the above code as examples!
# Print out the host name and power state
# Host API path is /api/vcenter/host
# If you get stuck, use the code in vcenter-REST-host.py to help you