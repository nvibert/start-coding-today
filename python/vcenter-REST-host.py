# This file will not run directly, this code is intended to be pasted into vcenter-REST.py.
# The student should be trying to figure out the code on their own and use this file as a reference if they get stuck.

vc_host_url = VC_NAME + '/api/vcenter/host'
response = requests.get(vc_host_url,headers=GET_HEADER)
host_json = response.json()
print('\n\nHosts found on vCenter',VC_NAME)
for host in host_json:
    print(host['name'],host['power_state'])