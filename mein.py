from argparse import FileType
import tkinter as tk
from tkinter import filedialog

def get():
    filetype_list=[("all file","*")]
    filepath =filedialog.askopenfilename(initialdir="/",filetypes =filetype_list)
    print(filepath)
    message["text"]=filepath

root= tk.Tk()
root.title("タイトルです")
root.geometry("300x300")

message  =tk.Message(root,text="file_path",width=600)
bt=tk.Button(text="ファイルダイアログ",command=get)
message.pack()
bt.pack()

root.mainloop()
