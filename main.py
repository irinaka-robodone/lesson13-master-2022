
import tkinter as tk
from tkinter import Label, filedialog
from tkinter import messagebox

def get_filepath():
    filetype_list=[("all fine","*")]
    filetype=filedialog.askopenfilename(initialdir="/",filetypes=filetype_list)
    print(filepath)
    message["text"]=filepath

def msg_info():
    ret=label["text"]=str(messagebox.showinfo("info","インフォメーション"))
    print(ret)

def msg_warning():
    ret=label["text"]=str(messagebox.showwarning("warning","警告"))
    print(ret)

def msg_error():
    ret=label["text"]=str(messagebox.showerror("error","エラーです！"))
    print(ret)

def msg_question():
    ret=label["text"]=str(messagebox.askquestion("question","質問です！"))
    print(ret)

def msg_yesno():
    ret=messagebox.askyesno("yesno","はい？いいえ？どちらですか？")
    print(ret)
    if ret==True:
        label["text"]="yes"
    else:
        label["text"]="no"

def msg_okcancel():
    ret=messagebox.askokcancel("okcancel","OK？Cancel？どちらですか？")
    print(ret)
    if ret==True:
        label["text"]="Ok"
    else:
        label["text"]="cancel"

def msg_retrycannel():
    ret=messagebox.askretrycancel("retrycancel","リトライ？Cancel？どちらですか？")
    print(ret)
    if ret==True:
        label["text"]="retry"
    else:
        label["text"]="cancel"

root = tk.Tk()
root.title("実験")
root.geometry("800x400")

message=tk.Message(root,text="file_path",width=600)

bt=tk.Button(text="ファイルダイアログ",command=get_filepath)

label=tk.Label(text="レイアウト設定",background="yellow")
bt1=tk.Button(text="info",command=msg_info)
bt2=tk.Button(text="warning",command=msg_warning)
bt3=tk.Button(text="error",command=msg_error)
bt4=tk.Button(text="question",command=msg_question)
bt5=tk.Button(text="yesno",command=msg_yesno)
bt6=tk.Button(text="okcancel",command=msg_okcancel)
bt7=tk.Button(text="retrycancel",command=msg_retrycannel)

label00=tk.Label(text="row=0,column=0",relief="groove")
label01=tk.Label(text="row=0,column=1",relief="groove")
label02=tk.Label(text="row=0,column=2",relief="groove")

label10=tk.Label(text="row=1,column=0",relief="groove")
label11=tk.Label(text="row=1,column=1",relief="groove")
label12=tk.Label(text="row=1,column=2",relief="groove")

label20=tk.Label(text="row=2,column=0",relief="groove")
label21=tk.Label(text="row=2,column=1",relief="groove")
label22=tk.Label(text="row=2,column=2",relief="groove")

# message.pack()
# label.pack(padx=10,pady=100,ipadx=100,ipady=10,fill="x",expand=True)
# bt.pack()

label00.grid(row=0,column=0)
label01.grid(row=0,column=1)
label02.grid(row=0,column=2)

label10.grid(row=1,column=0)
label11.grid(row=1,column=1)
label12.grid(row=1,column=2)

label20.grid(row=2,column=0)
label21.grid(row=2,column=1)
label22.grid(row=2,column=2)

#bt1.pack()
#bt2.pack()
#bt3.pack()
#bt4.pack()
#bt5.pack()
#bt6.pack()
#bt7.pack()

root.mainloop()