from tkinter import Tk, Canvas, PhotoImage, Entry, Button, Label, END, messagebox
from password_generator import get_random_password
import pyperclip as ppc

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def populate_password():
    generated_pass = get_random_password()
    if len(password_entry.get()) > 0:
        password_entry.delete(0, END)
        password_entry.insert(0, generated_pass)
    else:
        password_entry.insert(0, generated_pass)
    ppc.copy(generated_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #

website_data = ''
email_username_data = ''
password_data = ''


def add_data():
    global website_data, email_username_data, password_data
    website_data = website_entry.get()
    email_username_data = email_Username_entry.get()
    password_data = password_entry.get()
    if check_user_data():
        is_data_ok = messagebox.askokcancel(title='IS DATA OK', message=f'The Details entered are \n Website: '
                                                                        f'{website_data} \n Username-Email: '
                                                                        f'{email_username_data} \n Password: '
                                                                        f'{password_data}')
        if is_data_ok:
            with open('data.txt', "a") as data_file:
                data_file.write(f'{website_data} | {email_username_data} | {password_data}\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        else:
            pass
    else:
        messagebox.showinfo(title='OOPS', message='Please don\'t leave any field empty')


def check_user_data():
    if len(website_data) > 0 and len(email_username_data) > 0 and len(password_data) > 0:
        return True
    else:
        return False

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

logo_cv = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
logo_cv.create_image(100, 100, image=logo_image)
logo_cv.grid(row=0, column=1)

website = Label(text='Website:')
website.grid(column=0, row=1)

email_Username = Label(text='Email/Username:')
email_Username.grid(column=0, row=2)

password = Label(text='Password')
password.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_Username_entry = Entry(width=35)
email_Username_entry.grid(column=1, row=2, columnspan=2)
email_Username_entry.insert(0, 'mayheptad@onenewspace.com')

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

gen_pass_btn = Button(text='Generate Password', command=populate_password)
gen_pass_btn.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=add_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
