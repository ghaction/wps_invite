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

    info = '''<p>昵称:<font color="blue">{nickname}</font></p>
<p>用户ID:<font color="blue">{userid}</font></p>
<p>用户类型:<font color="blue">{user_type}</font></p>
    '''.format(nickname=nickname, userid=userid, regtime=regtime, user_type=user_type)

    try:
        vip_expire_time = "<p>---------会员到期时间---------</p>"
        for i in response.json().get("data").get("vip").get("enabled"):
            vip_expire_time = vip_expire_time + "<p>" + i.get("name") + ":" + time.strftime('%Y-%m-%d %H:%M:%S',
                                                                                            time.gmtime(i.get(
                                                                                                "expire_time"))) + "</p>"
        info = info + "<p>" + vip_expire_time
    except:
        pass

    return info


def get_data(wps_sid):
    url = "https://zt.wps.cn/2018/clock_in/api/get_data?member=wps"
    wps_sid = str(wps_sid)
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'Host': 'zt.wps.cn',
        'sid': wps_sid,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, timeout=2000)
    response = response.json()
    total_add_day = str(response.get("total_add_day"))
    invite_count = str(response.get("invite_count"))
    today_extra_reward = str(response.get("today_extra_reward"))
    yesterday_extra_reward = str(response.get("yesterday_extra_reward"))
    inf = '''<p>------------邀请信息------------</p>
<p>总获得天数:<font color="blue">{total_add_day}</font>天</p>
<p>今天邀请次数:<font color="blue">{invite_count}</font>次</p>
<p>邀请获得天数:<font color="blue">{today_extra_reward}</font>天</p>
<p>昨天邀请天数:<font color="blue">{yesterday_extra_reward}</font>天</p>
    '''.format(total_add_day=total_add_day, invite_count=invite_count, today_extra_reward=today_extra_reward,
               yesterday_extra_reward=yesterday_extra_reward)
    return inf
