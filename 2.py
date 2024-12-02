from tkinter import *
from tkinter import messagebox
win = Tk()
win.geometry('500x500')
win.title('Hacker666 App')
win.configure(bg='red')
# Functions
def clear():
    ent_e1.delete(0, END)
    ent_e2.delete(0, END)
    ent_e3.delete(0, END)
    ent_e4.delete(0, END)
    ent_e1.focus_set()
def exit():
    result = messagebox.askyesno('Closing', 'Are you sure you want to close this window?')
    if result:
        win.destroy()
def insert():
    first_name = ent_e1.get().strip()
    last_name = ent_e2.get().strip()
    score = ent_e3.get()
    
    # Check if first name and last name contain only letters
    if not first_name.isalpha():
        messagebox.showerror('Input Error', 'Please do not use numbers in the First Name field.')
        return
    if not last_name.isalpha():
        messagebox.showerror('Input Error', 'Please do not use numbers in the Last Name field.')
        return
    if not first_name or not last_name:
        messagebox.showerror('Input Error', 'Please fill in both First Name and Last Name.')
        return
    
    if score.isdigit():
        if 0 <= int(score) <= 20:
            lst_l1.insert(END, f'{first_name}, {last_name}, {score}, {ent_e4.get()}')
            clear()
        else:
            messagebox.showerror('Incorrect Score', 'Please enter a number between 0 and 20')
    else:
        messagebox.showerror('Incorrect Score', 'Please enter a number')
def delete():
    selection = lst_l1.curselection()
    if selection:
        confirmation = messagebox.askyesno("Delete Confirmation", "Are you sure you want to delete the selected item?")
        if confirmation:
            lst_l1.delete(selection)
    else:
        messagebox.showerror('Delete Error', 'No item selected for deletion')
def fetch():
    selection = lst_l1.curselection()
    if not selection:
        messagebox.showwarning('Selection Error', 'Please select an item to fetch.')
        return
    selected_item = lst_l1.get(selection)
    a, b, c, d = selected_item.split(', ')
    
    clear()  # Clear the entries before inserting new values
    ent_e1.insert(0, a)
    ent_e2.insert(0, b)
    ent_e3.insert(0, c)
    ent_e4.insert(0, d)
# Widgets
lbl_a1 = Label(text='First Name:', bg='darkblue', fg='white')
lbl_a1.grid(row=0, column=1, pady=10, padx=5)
lbl_a2 = Label(text='Last Name:', bg='darkblue', fg='white')
lbl_a2.grid(row=0, column=4, pady=10, padx=5)
lbl_a3 = Label(text='Score:', bg='darkblue', fg='white')
lbl_a3.grid(row=1, column=1, pady=10, padx=5)
lbl_a4 = Label(text='Tel:', bg='darkblue', fg='white')
lbl_a4.grid(row=1, column=4, pady=10, padx=5)
btn_b1 = Button(text='Insert', bg='green', fg='white', command=insert)
btn_b1.place(x=60, y=400)
btn_b2 = Button(text='Clear', bg='green', fg='white', command=clear)
btn_b2.place(x=130, y=400)
btn_b3 = Button(text='Delete', bg='green', fg='white', command=delete)
btn_b3.place(x=200, y=400)
btn_b4 = Button(text='Fetch', bg='green', fg='white', command=fetch)
btn_b4.place(x=270, y=400)
btn_b5 = Button(text='Exit', bg='green', fg='white', command=exit)
btn_b5.place(x=170, y=360)
ent_e1 = Entry(win)
ent_e1.grid(row=0, column=2)
ent_e2 = Entry(win)
ent_e2.grid(row=0, column=5)
ent_e3 = Entry(win)
ent_e3.grid(row=1, column=2)
ent_e4 = Entry(win)
ent_e4.grid(row=1, column=5)
lst_l1 = Listbox(width=60, height=10)
lst_l1.place(x=40, y=200)
sb = Scrollbar(win)
sb.place(x=345, y=203, height=150)
lst_l1.config(yscrollcommand=sb.set)
sb.config(command=lst_l1.yview)
win.mainloop()