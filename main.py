
import tkinter as tk
from tkinter import Label, filedialog
from tkinter import messagebox

def get_filepath():
    filetype_list=[("all fine","*")]
    filetype=filedialog.askopenfilename(initialdir="/",filetypes=filetype_list)
    print(filepath)
    message["text"]=filepath

def callback_func(event):
    label["text"]=event.keysym

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
root.title("キーボード入力")
root.geometry("800x400")

label=tk.Label(root,text="keysym",relief="groove")

canvas = tk.Canvas(root,width=500,height=500,bg="lime green")
canvas_2 = tk.Canvas(root,width=200,height=30,bg="orange")
canvas.pack()
canvas_2.place(x=300,y=200)

frame1=tk.Frame(root,width=700,height=400,background="red")
frame2=tk.Frame(root,width=700,height=400,background="yellow")

message=tk.Message(root,text="file_path",width=600)

bt=tk.Button(text="ファイルダイアログ",command=get_filepath)

#label=tk.Label(text="レイアウト設定",background="yellow")
bt1=tk.Button(text="info",command=msg_info)
bt2=tk.Button(text="warning",command=msg_warning)
bt3=tk.Button(text="error",command=msg_error)
bt4=tk.Button(text="question",command=msg_question)
bt5=tk.Button(text="yesno",command=msg_yesno)
bt6=tk.Button(text="okcancel",command=msg_okcancel)
bt7=tk.Button(text="retrycancel",command=msg_retrycannel)

label00=tk.Label(frame1,text="row=0,column=0",relief="groove")
label01=tk.Label(frame1,text="row=0,column=1",relief="groove")
label02=tk.Label(frame1,text="row=0,column=2",relief="groove")

label10=tk.Label(frame1,text="row=1,column=0",relief="groove")
label11=tk.Label(frame1,text="row=1,column=1",relief="groove")
label12=tk.Label(frame1,text="row=1,column=2",relief="groove")

label00_2=tk.Label(frame2,text="row=0,column=0",relief="groove")
label01_2=tk.Label(frame2,text="row=0,column=1",relief="groove")
label02_2=tk.Label(frame2,text="row=0,column=2",relief="groove")

label10_2=tk.Label(frame2,text="row=1,column=0",relief="groove")
label11_2=tk.Label(frame2,text="row=1,column=1",relief="groove")
label12_2=tk.Label(frame2,text="row=1,column=2",relief="groove")

# label=tk.Label(frame1,text="四角1",background="white")
# label.place(x=25,y=25,width=50,height=50)

# label=tk.Label(frame1,text="四角2",background="white")
# label.place(x=350,y=100,width=230,height=200)

# label=tk.Label(frame2,text="四角3",background="white")
# label.place(x=25,y=25,width=50,height=50)

# label=tk.Label(frame2,text="四角4",background="white")
# label.place(x=350,y=100,width=230,height=200)

# canvas.create_rectangle(20,40,150,300,fill="red",outline="blue",width=3)
# canvas.create_oval(100,100,350,250,fill="blue",outline="white",width=10)
# canvas.create_line(450,50,40,300,150,370,100,450,fill="blue",width=3)

# canvas.create_text(100,400,text="プログラミング",font=("Helvetica",18,"bold"),angle=-30)
# canvas.create_text(400,60,text="ロボット制作",font=("Helvetica",18,"bold"),angle=90)
# canvas.create_text(400,400,text="ロボ団",font=("Heletica",18,"bold"),angle=180)

root.bind("<Key>",callback_func)

# message.pack()
label.pack()
# bt.pack()

# label00.grid(row=0,column=0,columnspan=3)
# label10.grid(row=0,column=1)
# label11.grid(row=0,column=2)
# label12.grid(row=1,column=0)

# label00_2.grid(row=0,column=0,rowspan=2)
# label01_2.grid(row=0,column=1)

# label10_2.grid(row=0,column=2)
# label11_2.grid(row=1,column=1)
# label12_2.grid(row=1,column=2)

# frame1.pack()
# frame2.pack()

# bt1.pack()
# bt2.pack()
# bt3.pack()
# bt4.pack()
# bt5.pack()
# bt6.pack()
# bt7.pack()




root.mainloop()