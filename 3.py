from tkinter import *

root = Tk()
root.geometry('350x350')


def change_color():
    selection = v.get()
    if selection == 1:
        root.configure(bg='red')
    elif selection == 2:
        root.configure(bg='blue')
    elif selection == 3:
        root.configure(bg='green')


def run_action():
    change_color()


v = IntVar()
options = {"Red Color": 1, "Blue Color": 2, "Green Color": 3}



for txt, val in options.items():
    Radiobutton(root, text=txt, variable=v, value=val).pack(side=TOP, pady=4)  # اضافه کردن RadioButton

run_button = Button(root, text="Run", command=run_action)

run_button.pack(side=TOP, pady=10)


root.mainloop()