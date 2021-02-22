def sendmail(mailtitle, mailbody):  # (标题，正文)
    from email.mime.text import MIMEText
    from email.utils import formataddr
    import smtplib
    import os
    import json

    if os.path.exists("config.json"):
        f = open('config.json', 'r')
        config = f.read()
        f.close()
        config = json.loads(config)
        enable_email=config.get("mail").get("enable_email")
        smtp_sever = config.get("mail").get("smtp_sever")
        from_addr = config.get("mail").get("email_addr")
        password=config.get("mail").get("password")
        to_addr=config.get("mail").get("to_addr")
    else:
        # SMTP服务器以及相关配置信息
        enable_email=os.environ["enable_email"]
        smtp_sever = os.environ["STMP_SERVER"]
        from_addr = os.environ["FROM_ADDR"]  # 发件人邮箱
        password = os.environ["MAIL_PASSWORD"]  # 授权码
        to_addr = os.environ["TO_ADDR"]  # 收件人邮箱

    from_username = "massage robot"  # 发件人昵称
    if mailtitle is None:
        mailtitle = 'WPS'  # 默认邮件标题

    # 邮件正文

    msg = MIMEText(mailbody, 'html', 'utf-8')
    msg['From'] = formataddr((from_username, from_addr))  # 发件人昵称和邮箱
    msg['To'] = formataddr(('', to_addr))  # 收件人昵称和邮箱
    msg['Subject'] = mailtitle  # 邮件标题

    if enable_email == "true":
        server = smtplib.SMTP_SSL(smtp_sever, 465)
        server.login(from_addr, password)
        # 发送邮件
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.quit()
    else:
        print("邮件未启用")



