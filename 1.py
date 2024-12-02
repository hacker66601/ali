from tkinter import *
root = Tk()
root.geometry('400x400')
def change_color():
    selection = v.get()
    if selection == 1:
        root.configure(bg='red')   # رنگ پس‌زمینه قرمز برای OptionButton A
    elif selection == 2:
        root.configure(bg='blue')  # رنگ پس‌زمینه آبی برای OptionButton B
    elif selection == 3:
        root.configure(bg='green') # رنگ پس‌زمینه سبز برای OptionButton C
v = IntVar()
options = {"OptionButton A" : 1, "OptionButton B" : 2, "OptionButton C": 3}
for txt, val in options.items():
    Radiobutton(root, text=txt, variable=v, value=val, command=change_color).pack(side=TOP, pady=4) # اضافه کردن command
root.mainloop()