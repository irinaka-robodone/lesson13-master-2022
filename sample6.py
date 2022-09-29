import tkinter as tk
root=tk.Tk()

canvas=tk.Canvas(root, width=500, height=500, bg="lime green")

canvas.pack()

canvas.create_rectangle(20,40,150,300, fill="red", outline="blue", width=3)

canvas.create_oval(100,100,350,250, fill="blue", outline="white", width=10)

canvas.create_line(450,50,450,300,150,370,100,450, fill="blue",  width=3)

canvas.create_text(100,400, text="プログラミング", font=("Helvetica",18,"bold"),angle=-30)
canvas.create_text(400,60, text="ロボット製作", font=("Helvetica",18,"bold"),angle=90)
canvas.create_text(400,400, text="ロボ団", font=("Helvetica",18,"bold"),angle=180)

root.mainloop()
