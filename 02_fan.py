#coding=utf-8
import json
import requests
import urllib.request,urllib.parse

headers ={
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}
post_data = {
    "query":"人生苦短",
    "from":"zh",
    "to":"en",
}

post_url = "http://fanyi.baidu.com/basetrans"
r = requests.post(post_url,data=post_data,headers=headers)
print(r.content.decode('unicode-escape'))
dict_ret = json.loads(r.content.decode())
print(dict_ret)
ret = dict_ret["trans"][0]["dst"]
print("reuslt is :",ret)