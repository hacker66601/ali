from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db = Database('D:/test1/contacts Manager.db')

def populate_list():
    contact_list.delete(0, END)
    record = db.fetch()
    for row in record:
        contact_list.insert(END, f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}')  # اضافه کردن شماره تلفن

def add_items():
    if name_entry.get() == '' or family_entry.get() == '' or address_entry.get() == '' or phone_entry.get() == '':
        messagebox.showerror("خطا", "لطفا ورودی ها را کامل کنید")
        return

    db.insert(name_entry.get(), family_entry.get(), address_entry.get(), phone_entry.get())
    clear_text()
    populate_list()

def delete_item():
    try:
        index = contact_list.curselection()[0]
        contact = contact_list.get(index).split(', ')
        db.remove(contact[0], contact[1])  # Assuming first two fields are name and family
        populate_list()
    except IndexError:
        messagebox.showerror("خطا", "لطفا یک مورد را انتخاب کنید")

def update_item():
    try:
        index = contact_list.curselection()[0]
        contact = contact_list.get(index).split(', ')
        db.update(name_entry.get(), family_entry.get(), address_entry.get(), phone_entry.get())
        clear_text()
        populate_list()
    except IndexError:
        messagebox.showerror("خطا", "لطفا یک مورد را انتخاب کنید")

def clear_text():
    name_entry.delete(0, END)
    family_entry.delete(0, END)
    address_entry.delete(0, END)
    phone_entry.delete(0, END)

def show_contact(event):
    try:
        index = contact_list.curselection()[0]
        contact = contact_list.get(index).split(', ')
        name_entry.delete(0, END)
        family_entry.delete(0, END)
        address_entry.delete(0, END)
        phone_entry.delete(0, END)

        name_entry.insert(0, contact[0])
        family_entry.insert(0, contact[1])
        address_entry.insert(0, contact[2])
        phone_entry.insert(0, contact[3])
    except IndexError:
        pass

def search_items():
    search_term = search_entry.get()
    contact_list.delete(0, END)
    record = db.search(search_term)  # Assuming db.search is implemented
    for row in record:
        contact_list.insert(END, f'{row[0]}, {row[1]}, {row[2]}, {row[3]}')

# Set up the GUI
root = Tk()
root.title("مدیر تماس")

# Create labels and entry fields
name_label = Label(root, text="نام")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = Entry(root)
name_entry.grid(row=0, column=1)

family_label = Label(root, text="نام خانوادگی")
family_label.grid(row=1, column=0, padx=10, pady=10)
family_entry = Entry(root)
family_entry.grid(row=1, column=1)

address_label = Label(root, text="آدرس")
address_label.grid(row=2, column=0, padx=10, pady=10)
address_entry = Entry(root)
address_entry.grid(row=2, column=1)

phone_label = Label(root, text="شماره تلفن")
phone_label.grid(row=3, column=0, padx=10, pady=10)
phone_entry = Entry(root)
phone_entry.grid(row=3, column=1)

# Create the contact listbox
contact_list = Listbox(root, height=10, width=50)
contact_list.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
contact_list.bind('<<ListboxSelect>>', show_contact)

# Create control buttons
add_button = Button(root, text="اضافه کردن", command=add_items)
add_button.grid(row=5, column=0, padx=10, pady=10)

delete_button = Button(root, text="حدف کردن", command=delete_item)
delete_button.grid(row=5, column=1, padx=10, pady=10)

update_button = Button(root, text="بروزرسانی", command=update_item)
update_button.grid(row=6, column=0, padx=10, pady=10)

clear_button = Button(root, text="پاک کردن ورودی ها", command=clear_text)
clear_button.grid(row=6, column=1, padx=10, pady=10)

search_entry = Entry(root)
search_entry.grid(row=7, column=0, padx=10, pady=10)

search_button = Button(root, text="جستجو", command=search_items)
search_button.grid(row=7, column=1, padx=10, pady=10)

populate_list()  # Fill the list with existing contact records

root.mainloop()
