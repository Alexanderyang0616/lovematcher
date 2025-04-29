import tkinter as tk
from tkinter import messagebox
import time

def submit():
    name = entry_name.get()
    city = entry_city.get()

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
