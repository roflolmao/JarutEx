import tkinter as tk
app=tk.Tk()
app.title("ตัวอย่าง Spinbox")
app.geometry("320x240")

spin_val = tk.IntVar()
spin_val.set(4) # ค่าเริ่มต้น
spin_box = tk.Spinbox(app,
			textvariable=spin_val,
			from_=0, to=9,
			increment=1)
spin_box.pack()
app.mainloop()
