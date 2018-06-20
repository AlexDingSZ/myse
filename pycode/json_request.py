import json
import requests

posturl = "http://test.xhqb.com/auth/pass/sendpass"
data = {"phoneNum":"15013335555","deviceID":"1c121817","bizType":"login"}
headers = {"Content-Type":"application/json"}
r = requests.post(posturl,data=json.dumps(data), headers=headers)
print(r.text)
respcontent = json.loads(r.content)
print(respcontent["resultCode"])
