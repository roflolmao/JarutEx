import tkinter as tk
app=tk.Tk()
app.title("ตัวอย่าง Listbox")
app.geometry("480x240")

def lbox_event(event):
    lbox_str.set(lbox.get(lbox.curselection()))  

lbox_str = tk.StringVar()
list_items = tk.Variable()
lbox = tk.Listbox(app, listvariable=list_items, 	
		width=50,height=11,
		font=('Tahoma',10),selectmode=tk.SINGLE)
lbox.insert(tk.END,"การลาป่วย")
lbox.insert(tk.END,"การลาคลอดบุตร")
lbox.insert(tk.END,"การลาไปช่วยภริยาที่คลอดบุตร")
lbox.insert(tk.END,"การลากิจส่วนตัว")
lbox.insert(tk.END,"การลาพักผ่อน")
lbox.insert(tk.END,"การลาอุปสมบท หรือการลาไปประกอบพิธฮัจย์")
lbox.insert(tk.END,"การลาเข้ารับการตรวจคัดเลือก หรือเข้ารับการเตรียมพล")
lbox.insert(tk.END,"การลาไปศึกษา ฝึกอบรม ดูงาน หรือปฏิบัติการวิจัย")
lbox.insert(tk.END,"การลาไปปฏิบัติงานในองค์การระหว่างประเทศ")
lbox.insert(tk.END,"การลาติดตามคู่สมรส")
lbox.insert(tk.END,"การลาไปฟื้นฟูสมรรถภาพด้านอาชีพ")
lbox.bind('<<ListboxSelect>>', lbox_event)
label = tk.Label(app,textvariable=lbox_str,width=50,height=2)
lbox.pack(ipadx=10,pady=10)
label.pack()
app.mainloop()
