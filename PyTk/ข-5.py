import tkinter as tk
count = 0
def clicked():
    global count
    count += 1
    lbl_str['text'] = f"{count}"
app = tk.Tk()
lbl_str = tk.Label(app, text="สวัสดี", font=("Tahoma",12))
btn_say = tk.Button(app, text="คลิก", font=("Tahoma",12),
			command=clicked)
lbl_str.pack()
btn_say.pack()
app.mainloop()
