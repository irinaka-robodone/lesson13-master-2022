import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("タイトルです")

ladel=tk.Label(text="レイアウト設定",background="yellow")

ladel.pack(padx=10,ipadx=100,ipady=10,fill="x",expand=True)
root.mainloop()
