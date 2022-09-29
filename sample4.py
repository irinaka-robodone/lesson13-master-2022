from tkinter import Tk


import tkinter as tk

root = tk.Tk()
root.title("タイトルです")
root.geometry("500x500")

label00=tk.Label(text="row=0,column=0",relief="groove")
label01=tk.Label(text="row=0,column=1",relief="groove")
label02=tk.Label(text="row=0,column=2",relief="groove")

label10=tk.Label(text="row=1,column=0",relief="groove")
label11=tk.Label(text="row=1,column=1",relief="groove")
label12=tk.Label(text="row=1,column=2",relief="groove")

label20=tk.Label(text="row=2,column=0",relief="groove")
label21=tk.Label(text="row=2,column=1",relief="groove")
label22=tk.Label(text="row=2,column=2",relief="groove")

label00.grid(row=0,column=0)
label01.grid(row=0,column=1)
label02.grid(row=0,column=2)

label10.grid(row=1,column=0)
label11.grid(row=1,column=1)
label12.grid(row=1,column=2)

label20.grid(row=2,column=0)
label21.grid(row=2,column=1)
label22.grid(row=2,column=2)

root.mainloop()
