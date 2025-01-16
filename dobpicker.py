from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("600x400")
root.title("Set DOB")

def getdata():
    day = day_var.get()
    month = month_var.get()
    year = year_var.get()
    if day and month and year:
        output_box.delete("1.0", END)
        date = day + "/" + month + "/" + year
        output_box.insert("1.0", date.center(50))
        output_box.tag_configure("center", justify="center")
        output_box.tag_add("center", "1.0", "end")

def on_select(event):
    getdata()

day_var = StringVar()
month_var = StringVar()
year_var = StringVar()

days = [str(i) for i in range(1, 31)]
months = [str(i) for i in range(1, 12)]
years = [str(i) for i in range(1925, 2024)]

Label(root, text="DD", font=("Helvetica", 10, "bold")).place(x=10, y=20)
day_combobox = ttk.Combobox(root, textvariable=day_var, values=days, width=5)
day_combobox.place(x=50, y=20)
day_combobox.bind("<<ComboboxSelected>>", on_select)

Label(root, text="MM", font=("Helvetica", 10, "bold")).place(x=150, y=20)
month_combobox = ttk.Combobox(root, textvariable=month_var, values=months, width=5)
month_combobox.place(x=190, y=20)
month_combobox.bind("<<ComboboxSelected>>", on_select)

Label(root, text="YYYY", font=("Helvetica", 10, "bold")).place(x=300, y=20)
year_combobox = ttk.Combobox(root, textvariable=year_var, values=years, width=7)
year_combobox.place(x=350, y=20)
year_combobox.bind("<<ComboboxSelected>>", on_select)

output_box = Text(root, width=50, height=10, bd=3)
output_box.place(x=50, y=80)
output_box.tag_configure("center", justify="center")

root.mainloop()
