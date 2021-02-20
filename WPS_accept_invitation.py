from time import sleep
import os
import random
import requests

invite_userid = os.environ["USERID"]
sids = os.environ["SIDS"]

invite_userid = invite_userid.split(',')
sids = sids.split(',')

url = "https://zt.wps.cn/2018/clock_in/api/invite"
payload = {'invite_userid': '1136976999'}

num1 = 0
for x in invite_userid:
    n1 = 0
    n2 = 0
    num1 = num1 + 1
    mail_body = ""
    print("-----第" + str(num1) + "个ID-----")
    for i in sids:
        headers = {
            'Accept-Language': 'zh-cn',
            'sid': x,
            'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; Mi-4c Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN miniProgram'
        }

        response = requests.request("POST", url, headers=headers, data=payload, timeout=2000)
        try:
            return_result = (response.json().get("result"))

            if return_result == "ok":
                n1 = n1 + 1
                mail_body = mail_body + "<P><STRONG>" + str(x) + "," + str(
                    i) + ",<FONT color=#008000>成功!</FONT></STRONG></P>"
                print("成功！ " + str(n1))
            else:
                msg = (response.json().get("msg"))
                n2 = n2 + 1

                mail_body = mail_body + "<P><STRONG>" + str(x) + "," + str(
                    i) + ",<FONT color=#ff0000>失败!</FONT>" + msg + "</STRONG></P>"
                print("失败！ " + str(n2))
        except:
            pass  # 占位符

        sleep(random.uniform(1, 5))

mail_body = "<P><STRONG>-------------</STRONG></P><P><STRONG>成功:<FONT color=#008000>" + str(
    n1) + "</FONT></STRONG></P><P><STRONG>失败:<FONT color=#ff0000>" + str(
    n2) + "</FONT></STRONG></P><P><STRONG>-------------</STRONG></P></BODY></HTML>" + mail_body

print("----------\n总计:\n成功" + str(n1) + "次\n失败" + str(n2) + "次\n----------")
# 发送邮件通知
import smail

smail.sendmail(mail_body)
