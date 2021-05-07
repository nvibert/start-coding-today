#!/bin/sh
# Author: Alan Renouf
# Product: VMware Cloud on AWS
# Description: Sample CURL statement for using the VMware Cloud on AWS APIs
# Obtain your refresh_token used to get a valid authentication token which can be obtained after successful login to the following URL via a web browser: https://console.cloud.vmware.com/csp/gateway/portal/#/user/account. 
REFRESH_TOKEN=xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx

# Login with Refresh token and store Access token for future calls
AUTH_RESPONSE=$(curl -s -X POST "https://console.cloud.vmware.com/csp/gateway/am/api/auth/api-tokens/authorize" -H "accept: application/json" -H "content-type: application/x-www-form-urlencoded" -d "refresh_token=$REFRESH_TOKEN")
ACCESS_TOKEN=$(echo $AUTH_RESPONSE | awk -F '"access_token":"' '{print $2}' | awk -F '","' '{print $1}')

# List Orgs
curl -s -X GET -H "Content-Type: application/json" "https://vmc.vmware.com/vmc/api/orgs" -H "csp-auth-token: $ACCESS_TOKEN"