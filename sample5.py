import tkinter as tk

root = tk.Tk()
root.title("タイトルです")
root.geometry("500x500")

frame1=tk.Frame(root,background="#ece")
frame2=tk.Frame(root,background="blue")

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

label00_2.grid(row=0,column=0,rowspan=1)
label01_2.grid(row=0,column=1)
label02_2.grid(row=0,column=2)
label11_2.grid(row=1,column=1)
label12_2.grid(row=1,column=2)

label00.grid(row=0,column=0,columnspan=1)
label01.grid(row=1,column=0)
label11.grid(row=1,column=1)
label12.grid(row=1,column=2)

frame1.pack(padx=15,pady=15)
frame2.pack(padx=15,pady=15)
root.mainloop()
