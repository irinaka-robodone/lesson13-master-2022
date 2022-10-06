import tkinter as tk

root = tk.Tk()
root.title("タイトルです")
root.geometry("600x400")


frame1=tk.Frame(root,width=700,height=400,background="blue")
frame2=tk.Frame(root,width=700,height=400,background="blue")

label=tk.Label(frame1,text="四角1", background="white")
label.place(x=25,y=25,width=50,height=50)


label=tk.Label(frame1,text="四角2",background="white")
label.place(x=350,y=100,width=250,height=200)

frame1.pack()

canvas = tk.Canvas(root,width=500,height=500,bg="lime green")
canvas.pack()

canvas.create_rectangle(20,40, 150, 300,fill="red",outlined="blue",)


root.mainloop()
