
import tkinter as tk
from tkinter import filedialog

def get_filepath():
    filetype_list=[("all fine","*")]
    filetype=filedialog.askopenfilename(initialdir="/",filetypes=filetype_list)
    print(filepath)
    message["text"]=filepath

root=tk.Tk()
root.title("実験")
root.geometry("300x300")

message=tk.Message(root,text="file_path",width=600)
bt=tk.Button(text="ファイルダイアログ",command=get_filepath)

message.pack()
bt.pack()

root.mainloop()
































