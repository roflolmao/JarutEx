import tkinter as tk
app = tk.Tk()
app.title("ตัวอย่าง checkbutton")
app.geometry("320x240")
def cbx_clicked():
    msg.set(str(cb1_value.get())+" "+str(cb2_value.get()))
cb1_value = tk.IntVar()
cb2_value = tk.IntVar()
msg = tk.StringVar()
msg.set(str(cb1_value.get())+" "+str(cb2_value.get()))
label = tk.Label(app, textvariable=msg, width=40, height=2,font=("Tahoma",10))
chbx1 = tk.Checkbutton(app, command=cbx_clicked, variable=cb1_value,
			onvalue=1, offvalue=0, width=40, height=2,
			text="สำเนาทะเบียนบ้าน", font=("Tahoma",10))
chbx2 = tk.Checkbutton(app, command=cbx_clicked,variable=cb2_value,
			onvalue=1, offvalue=0, width=40, height=2,
			text="สำเนาบัตรประชาชน", font=("Tahoma",10))
chbx1.pack()
chbx2.pack()
label.pack()
app.mainloop()
