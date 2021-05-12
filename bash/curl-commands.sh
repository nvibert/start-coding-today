# These commands are examples to use against a local installation of vcsim
# curl -k -X POST -H "vmware-use-header-authn: string" -H "Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=" https://localhost:8989/rest/com/vmware/cis/session
# curl -k -H "vmware-api-session-id: e4821a1f-75a1-46f1-af7b-4fcdb16dd6cb" https://localhost:8989/rest/vcenter/folder

# These commmands demonstrate a login to a vCenter and a request to list vCenter folders
# -k indicates insecure - this allows you to connect to a homelab or other vCenter that doesn't have a valid certificate chain
# -i prints out the HTTP headers that the API responds with - useful to understand what's happening 
# -u lets you pass credentials in the form of username:password
# -X POST specifies that we want a POST instead of the default GET
# -c  specifies that you want all of the cookies written out to a textfile
# curl -k -i -u cloudadmin@vmc.local:password -X POST -c token.txt https://vcenterURL/rest/com/vmware/cis/session

# -k indicates insecure - this allows you to connect to a homelab or other vCenter that doesn't have a valid certificate chain
# -i prints out the HTTP headers that the API responds with - useful to understand what's happening 
# -b says to use a cookie file to pass cookies along with the request
# curl -k -i -b token.txt https://vcenterURL/rest/vcenter/folder`