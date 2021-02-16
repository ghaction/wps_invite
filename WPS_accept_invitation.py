from time import sleep
import os
import random
import requests

invite_userid = os.environ["USERID"]
sids = os.environ["SIDS"]

invite_userid = invite_userid.split(',')
sids = sids.split(',')

invite_url = 'http://zt.wps.cn/2018/clock_in/api/invite'

num1 = 0
for x in invite_userid:
    n1 = 0
    n2 = 0
    num1 = num1 + 1
    mail_body = ""
    print("-----第" + str(num1) + "个ID-----")
    for i in sids:
        rep = requests.post(invite_url, headers={"sid": i}, data={"invite_userid": x}, timeout=10)
        sleep(random.uniform(0.3, 1))
        try:
            return_result = (rep.json().get("result"))
            if return_result == "ok":
                n1 = n1 + 1
                mail_body = mail_body + "<P><STRONG>" + str(x) + "," + str(
                    i) + ",<FONT color=#008000>成功!</FONT></STRONG></P>"

                print("成功！ " + str(n1))
            else:
                n2 = n2 + 1

                mail_body = mail_body + "<P><STRONG>" + str(x) + "," + str(
                    i) + ",<FONT color=#ff0000>失败!</FONT></STRONG></P>"
                print("失败！ " + str(n2))
        except:
            pass

mail_body = "<P><STRONG>-------------</STRONG></P><P><STRONG>成功:<FONT color=#008000>" + str(
    n1) + "</FONT></STRONG></P><P><STRONG>失败:<FONT color=#ff0000>" + str(
    n2) + "</FONT></STRONG></P><P><STRONG>-------------</STRONG></P></BODY></HTML>" + mail_body

print("----------\n总计:\n成功" + str(n1) + "次\n失败" + str(n2) + "次\n----------")
# 发送邮件通知
import smail

smail.sendmail(mail_body)
