import requests
import os

invite_userid = os.environ["USERID"]

sids = (os.environ["SID"])

invite_url = 'http://zt.wps.cn/2018/clock_in/api/invite'

for i in sids:
    requests.post(invite_url, headers={'sid': i}, data={'invite_userid': invite_userid})
