# curl -k -X POST -H "vmware-use-header-authn: string" -H "Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=" https://localhost:8989/rest/com/vmware/cis/session
# curl -k -H "vmware-api-session-id: e4821a1f-75a1-46f1-af7b-4fcdb16dd6cb" https://localhost:8989/rest/vcenter/folder
# curl -k -i -u cloudadmin@vmc.local:password -X POST -c token.txt https://vcenterURL/rest/com/vmware/cis/session