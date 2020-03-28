import requests

proxies = {"http":"http://123.57.76.102:80"}
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/76.0.3809.87 Chrome/76.0.3809.87 Safari/537.36"
}
r = requests.get("https://www.google.com.hk/ ",proxies=proxies,headers=headers)
print(r.status_code)