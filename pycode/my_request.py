import  requests

# my_url="http://localhost/wordpress/readme.html"
#
# print(requests.get(my_url).text)
proxies = {"http": "http://127.0.0.1:8888"}
post_url = "http://localhost/wordpress/wp-login.php"
# POST http://localhost/wordpress/wp-login.php HTTP/1.1
# Host: localhost
# Connection: keep-alive
# Content-Length: 123
# Cache-Control: max-age=0
# Origin: http://localhost
# Upgrade-Insecure-Requests: 1
# Content-Type: application/x-www-form-urlencoded
# User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
# Referer: http://localhost/wordpress/wp-login.php?loggedout=true
# Accept-Encoding: gzip, deflate, br
# Accept-Language: zh-CN,zh;q=0.9
# Cookie: wordpress_test_cookie=WP+Cookie+check; _ga=GA1.1.1548068659.1513904798; optimizelyEndUserId=oeu1514939968713r0.16187427122280318; Idea-755a90e2=c80bec3a-01ec-4e4e-997c-3ed241eda69e; Pycharm-bdfc5fce=b735e692-bf93-4190-86be-35f5f7dc3d1f

my_header={"host":"localhost",
        "Connection":"keep-alive",
        "Content-Type":"application/x-www-form-urlencoded",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36",
        "Referer":"http://localhost/wordpress/wp-login.php?loggedout=true"

        }

headers ={"Host":"localhost",
          "Connection":"keep-alive",
          "Content-Type":"application/x-www-form-urlencoded",
          "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
          }
#Cookie: wordpress_test_cookie=WP+Cookie+check; _ga=GA1.1.1548068659.1513904798; optimizelyEndUserId=oeu1514939968713r0.16187427122280318; Idea-755a90e2=c80bec3a-01ec-4e4e-997c-3ed241eda69e; Pycharm-bdfc5fce=b735e692-bf93-4190-86be-35f5f7dc3d1f
# Cookie: wordpress_test_cookie=WP+Cookie+check; _ga=GA1.1.1548068659.1513904798;
# optimizelyEndUserId=oeu1514939968713r0.16187427122280318;
# Idea-755a90e2=c80bec3a-01ec-4e4e-997c-3ed241eda69e;
# Pycharm-bdfc5fce=b735e692-bf93-4190-86be-35f5f7dc3d1f

test_cookie={"wordpress_test_cookie":"WP+Cookie+check",
             "_ga":"GA1.1.1548068659.1513904798",
             "optimizelyEndUserId":"oeu1514939968713r0.16187427122280318",
             "Idea-755a90e2":"c80bec3a-01ec-4e4e-997c-3ed241eda69e",
             "Pycharm-bdfc5fce":"b735e692-bf93-4190-86be-35f5f7dc3d1f"

             }
test_cookie ={"wordpress_test_cookie":"WP+Cookie+check",
          "_ga":"GA1.1.1548068659.1513904798",
          "optimizelyEndUserId":"oeu1514939968713r0.16187427122280318",
          "Idea-755a90e2":"c80bec3a-01ec-4e4e-997c-3ed241eda69e"
          }
cookies ={"wordpress_test_cookie":"WP+Cookie+check",
              "_ga":"GA1.1.1548068659.1513904798",
              "optimizelyEndUserId":"oeu1514939968713r0.16187427122280318",
              "Idea-755a90e2":"c80bec3a-01ec-4e4e-997c-3ed241eda69e",
              "Pycharm-bdfc5fce":"b735e692-bf93-4190-86be-35f5f7dc3d1f"


}
#logs=admin&pwd=123456&wp-submit=%E7%99%BB%E5%BD%95&redirect_to=http%3A%2F%2Flocalhost%2Fwordpress%2Fwp-admin%2F&testcookie=1
param = {
    "logs":"admin",
    "pwd":"123456",
    "wp-submit": "%E7%99%BB%E5%BD%95",  #"wp-submit":"%E7%99%BB%E5%BD%95",
    #"redirect_to":"http%3A%2F%2Flocalhost%2Fwordpress%2Fwp-admin%2F",
    "testcookie":"1"}

headers ={"Host":"localhost",
          "Connection":"keep-alive",
          "Origin":"http://localhost",
          "Upgrade-Insecure-Requests":"1",
          "Content-Type":"application/x-www-form-urlencoded",
          "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36",
          "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
          "Referer":"http://localhost/wordpress/wp-login.php?loggedout=true",
          "Accept-Encoding":"gzip, deflate, br",
          "Accept-Language":"zh-CN,zh;q=0.9"

}
r=requests.post(post_url,data=param,headers=headers,cookies=cookies,proxies=proxies)



print(r.text)