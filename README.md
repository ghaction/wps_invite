https://github.com/datugou/WPS_daily_check_in



### 配置文件

```config.json```

### Repository secrets:```CONF```

```json
{
  "self": {
    "wps_sid": "自己的sid"
  },
  "userids": [
    "被邀请的用户ID"
  ],
  "invite": {
    "sids": [
      "第一个sid",
      "第二个sid",
      "第...个sid"
    ]
  },
  "mail": {
    "enable_email": "true",
    "smtp_sever": "smtp.xx.xx",
    "email_addr": "发送邮箱example@xx.xx",
    "password": "密码或授权码",
    "to_addr": "接收邮箱"
  }
}
```

