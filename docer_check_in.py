import requests
import os
import smail
import userinfo
print("-----------稻壳打卡-----------")
wps_sid = os.environ["wps_sid"]

url = "https://zt.wps.cn/2018/docer_check_in/api/checkin_today"

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'DNT': '1',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'wpsqing_autoLoginV1=1;uzone=CN-HN;ulocale=zh-CN;wps_sid=' + wps_sid
}

response = requests.request("POST", url, headers=headers, timeout=2000)
try:
    result = response.json().get("result")
    msg = response.json().get("msg")
    if result == "ok":
        mail_body = "稻壳签到成功！"
        print("签到成功!")
    if result == "error":
        if msg == "recheckin":
            mail_body = "已签到，无需重复签到！"
            print("已签到，无需重复签到！")
        elif msg == "no_login":
            mail_body = "Cookie错误！"
            print("未登录！")

except:
    mail_body = "错误：" + response.text
    print("其他错误！")

smail.sendmail("[稻壳签到结果]", userinfo.get_userinfo()+"---------------\n"+mail_body)  # 发送邮件通知
