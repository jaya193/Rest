from urllib.error import HTTPError

import requests
import json
url = 'https://dev93116.service-now.com/api/now/table/change_request'
#use the 'auth' parameter to send requests with HTTP Basic Auth:
#response = requests.get(url, auth = ("admin", "Ohd04QeZVNzd"))
#response = requests.get(url, auth = ("admin", "Ohd04QeZVNzd"),params={"sysparm_fields":["number","sys_id"],"sysparm_limit":"1"})
try:
    #response = requests.get(url,auth = ("admin", "Ohd04QeZVNzd"),params={"sys_id":"1766f1de47410200e90d87e8dee490f6"})
    response = requests.get(url, auth=("admin", "Ohd04QeZVNzd"),params={"sysparm_limit":"2"})
    if (response.status_code==200):
        jsonResponse = response.content
        print("Entire JSON response")
        #Json to python obj -->load
        json_object = json.loads(jsonResponse)
        #python obj to json -->dump
        print(json.dumps(json_object, indent=1))
        print("-------sysid------")
        #print(json_object["result"][0]["sys_id"])
        for i in json_object["result"]:
            print(i["sys_id"])
    else:
        print("***********")
        response.raise_for_status()
        print("something went wrong",response.status_code)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')




