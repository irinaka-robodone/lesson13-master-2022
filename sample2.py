
import tkinter as tk
from tkinter import messagebox

def infoo():
    ret=label["text"]=str(messagebox.showinfo("info","インフォメーションです"))
    print(ret)

def warningg():
    ret=label["text"]=str(messagebox.showinfo("warning","警告！"))
    print(ret)

def errorr():
    ret=label["text"]=str(messagebox.showinfo("error","エラーです！"))
    print(ret)

def auestionn():
    ret=label["text"]=str(messagebox.showinfo("auestion","質問です！"))
    print(ret)

def yesnoo():
    ret=messagebox.askyesno("yesno","はい？いいえ？どちらですか")
    print(ret)
    if ret == True:
        label["text"]="yes"
    else:
        label["text"]="no"

def okcancell():
    ret=messagebox.askokcancel("okcancel","OK？Cancel？どちらですか")
    print(ret)
    if ret == True:
        label["text"]="OK"
    else:
        label["text"]="cancel"
def retlrycancall():
    ret=messagebox.askyesno("retrycancal","リトライ？Cancal？どちらですか")
    print(ret)
    if ret == True:
        label["text"]="retry"
    else:
        label["text"]="cancal"
root =tk.Tk()
root.title("タイトルです")
root.geometry("300x500")

label=tk.Label(text="message")
bt1=tk.Button(text="info",command=infoo)
bt2=tk.Button(text="warning",command=warningg)
bt3=tk.Button(text="error",command=errorr)
bt4=tk.Button(text="auestion",command=auestionn)
bt5=tk.Button(text="yesno",command=yesnoo)
bt6=tk.Button(text="okcancel",command=okcancell)
bt7=tk.Button(text="retlrycancal",command=retlrycancall)
label.pack()
bt1.pack()
bt2.pack()
bt3.pack()
bt4.pack()
bt5.pack()
bt6.pack()
bt7.pack()
root.mainloop()
