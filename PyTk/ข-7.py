import tkinter as tk
def btn_clicked():
    my_str.set('สวัสดี'+txt_in.get())
    txt_in.focus_set()
    txt_in.delete(0, tk.END)
def txt_in_enter(n):
    btn_clicked()
app = tk.Tk()
app.title("โปรแกรมของฉัน")
app.geometry("320x200")
my_str = tk.StringVar(app)
my_str.set("ข้อความ")
label1 = tk.Label(text='กรุณากรอกชื่อ',font=('Tahoma',12))
label = tk.Label(textvariable=my_str,font=('Tahoma',12),fg='white', bg='blue', width=20, height=2)
btn = tk.Button(text="คลิก", font=('Tahoma',12),command=btn_clicked,width=20, height=2)
txt_in = tk.Entry(font=('Tahoma',12),width=20)
txt_in.bind('<Return>', txt_in_enter)
label1.pack()
txt_in.pack()
btn.pack()
label.pack()
txt_in.focus_set()
app.mainloop()
