import requests, random, os
from time import sleep

invite_userid = os.environ["USERID"]
sids = os.environ["SIDS"]

invite_userid = invite_userid.split(',')
sids = sids.split(',')

invite_url = 'http://zt.wps.cn/2018/clock_in/api/invite'

n1 = 0
n2 = 0
for x in invite_userid:
    for i in sids:
        rep = requests.post(invite_url, headers={"sid": i}, data={"invite_userid": x}, timeout=10)
        sleep(random.uniform(0.3, 1))
        try:
            return_result = (rep.json().get("result"))
            if return_result == "ok":

                n1 = n1 + 1
                print("成功！ " + str(n1))
            else:
                n2 = n2 + 1
                print("失败！ " + str(n2))
        except:
            pass

print("----------\n总计:\n成功" + str(n1) + "次\n失败" + str(n2) + "次\n----------")
