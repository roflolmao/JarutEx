import tkinter as tk
from tkinter import ttk
app=tk.Tk()
app.title("ตัวอย่าง Listbox+Scrollbar")
app.geometry("480x240")

def lbox_event(event):
    lbox_str.set(lbox.get(lbox.curselection()))
    
lbox_str = tk.StringVar()
list_items = tk.Variable()
lbox_Frame = tk.Frame(app)

lbox = tk.Listbox(lbox_Frame, listvariable=list_items,
			width=50,height=4,font=('Tahoma',10), selectmode=tk.SINGLE)

lbox.insert(tk.END, "การลาป่วย")
lbox.insert(tk.END, "การลาคลอดบุตร")
lbox.insert(tk.END, "การลาไปช่วยภริยาที่คลอดบุตร")
lbox.insert(tk.END, "การลากิจส่วนตัว")
lbox.insert(tk.END, "การลาพักผ่อน")
lbox.insert(tk.END, "การลาอุปสมบท หรือการลาไปประกอบพิธฮัจย์")
lbox.insert(tk.END, "การลาเข้ารับการตรวจคัดเลือก หรือเข้ารับการเตรียมพล")
lbox.insert(tk.END, "การลาไปศึกษา ฝึกอบรม ดูงาน หรือปฏิบัติการวิจัย")
lbox.insert(tk.END, "การลาไปปฏิบัติงานในองค์การระหว่างประเทศ")
lbox.insert(tk.END, "การลาติดตามคู่สมรส")
lbox.insert(tk.END, "การลาไปฟื้นฟูสมรรถภาพด้านอาชีพ")
lbox.bind('<<ListboxSelect>>', lbox_event)
label = tk.Label(app, textvariable=lbox_str, width=50,height=2)
lbox.pack( fill=tk.BOTH, expand=True, side=tk.LEFT)

scrollbar=ttk.Scrollbar(lbox_Frame, orient=tk.VERTICAL, command=lbox.yview)
lbox['yscrollcommand'] = scrollbar.set
scrollbar.pack(side=tk.LEFT, expand=True, fill=tk.Y)

lbox_Frame.pack()
label.pack()
app.mainloop()
