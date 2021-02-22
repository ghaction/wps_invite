from time import sleep
import os
import random
import requests
import smail

print("-----------WPS邀请-----------")
invite_userid = os.environ["USERID"]
sids = os.environ["SIDS"]

invite_userid = invite_userid.split(',')
sids = sids.split(',')

url = "https://zt.wps.cn/2018/clock_in/api/invite"

num1 = 0
n1 = n2 = 0
mail_body = ""

for x in invite_userid:

    n1 = n2 = 0
    mail_body = ""
    num1 = num1 + 1

    print("-----第" + str(num1) + "个ID-----")
    for i in sids:
        headers = {
            'Accept-Language': 'zh-cn',
            'sid': i,
            'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; Mi-4c Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN miniProgram'
        }
        payload = {'invite_userid': x}

        response = requests.request("POST", url, headers=headers, data=payload, timeout=2000)
        try:
            return_result = (response.json().get("result"))  # 获取结果

            if return_result == "ok":
                n1 = n1 + 1
                mail_body = mail_body + "<P><STRONG>" + str(x) + "," + str(
                    i) + ",<FONT color=#008000>成功!</FONT></STRONG></P>"
                print("成功！ " + str(n1))
            else:
                msg = (response.json().get("msg"))  # 获取错误信息
                n2 = n2 + 1

                mail_body = mail_body + "<P><STRONG>" + str(x) + "," + str(
                    i) + ",<FONT color=#ff0000>失败!</FONT>" + "   错误信息:\"" + msg + "\"" + "</STRONG></P>"
                print("失败！ " + str(n2))
        finally:
            pass  # 占位符

        sleep(random.uniform(1, 5))

mail_body = "<P><STRONG>-------------</STRONG></P><P><STRONG>成功:<FONT color=#008000>" + str(
    n1) + "</FONT></STRONG></P><P><STRONG>失败:<FONT color=#ff0000>" + str(
    n2) + "</FONT></STRONG></P><P><STRONG>-------------</STRONG></P></BODY></HTML>" + mail_body

print("----------\n总计:\n成功" + str(n1) + "次\n失败" + str(n2) + "次\n----------")

smail.sendmail("[WPS邀请结果]",mail_body)  # 发送邮件通知
