import tkinter as tk
def btn_clicked():
    my_str.set("นวัตกรรมคอมพิวเตอร์")
app = tk.Tk()
app.title("โปรแกรมของฉัน")
app.geometry("320x200")
my_str = tk.StringVar(app)
my_str.set("ข้อความ")
label = tk.Label(textvariable=my_str, font=('Tahoma',12),
                 fg='white', bg='blue', width=20, height=2)
btn = tk.Button(text="คลิก", font=('Tahoma',12),
                 command=btn_clicked, width=20, height=2)
label.pack()
btn.pack()
app.mainloop()
