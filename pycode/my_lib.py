import requests

geturl= "http://localhost/wordpress/readme.html"
r = requests.get(geturl,)
print(r.text)
print(type(r))

import requests
headers ={"Host":"localhost",
           "Connection":"keep-alive",
          "Content-Type":"application/x-www-form-urlencoded",
          "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
          }

cookies ={"wordpress_test_cookie":"WP+Cookie+check",
          "_ga":"GA1.1.1548068659.1513904798",
          "optimizelyEndUserId":"oeu1514939968713r0.16187427122280318",
          "Idea-755a90e2":"c80bec3a-01ec-4e4e-997c-3ed241eda69e"}
proxies = {"http": "http://127.0.0.1:8888"}

param = {"logs":"admin","pwd":"888888","wp-submit":"%E7%99%BB%E5%BD%95","testcookie":"1"}
post_url = "http://localhost/wordpress/wp-login.php"
r=requests.post(post_url,data=param,headers=headers,cookies=cookies,proxies=proxies)
print(r.text)

import  json

posturl = "http://test.xhqb.com/auth/pass/sendpass"
data = {"phoneNum":"15013335555","deviceID":"1c121817","bizType":"login"}
headers = {"Content-Type":"application/json"}
r = requests.post(posturl,data=json.dumps(data), headers=headers)
print(r.text)
respcontent = json.loads(r.content)
print(respcontent["resultCode"])
