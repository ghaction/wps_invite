import requests
import time


def get_userinfo(wps_sid):
    url = "https://vip.wps.cn/userinfo"
    payload = {}
    user_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Cookie': 'wpsqing_autoLoginV1=1; uzone=CN-HN; ulocale=zh-CN; wps_sid=' + wps_sid,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload, timeout=2000)

    nickname = response.json().get("data").get("nickname")  # 昵称
    userid = str(response.json().get("data").get("userid"))  # 用户ID
    user_type = response.json().get("data").get("vip").get("name")  # 当前用户类型
    regtime = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(response.json().get("data").get("regtime")))  # 注册时间

    info = '''昵称:{nickname}
    用户ID:{userid}
    用户类型:{user_type}
    '''.format(nickname=nickname, userid=userid, regtime=regtime, user_type=user_type)

    try:
        vip_expire_time = "---会员到期时间---\n"
        for i in response.json().get("data").get("vip").get("enabled"):
            vip_expire_time = vip_expire_time + i.get("name") + ":" + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(
                i.get("expire_time"))) + "\n"
        info = info + vip_expire_time

    finally:
        pass

    return info
