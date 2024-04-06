import tkinter as tk
app = tk.Tk()
app.title("โปรแกรมของฉัน")
app.geometry("320x200")
label = tk.Label(text="นวัตกรรมคอมพิวเตอร์",
                 font=('Tahoma',12),
                 fg='white', bg='blue',
                 width=20, height=2)
label.pack()
app.mainloop()
