import json
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

website = ''
email_username = ''
password = ''


def add_data():
    global website, email_username, password

    website = website_entry.get()
    email_username = email_Username_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            'email': email_username,
            'password': password
        }
    }

    if check_user_data():
        is_data_ok = messagebox.askokcancel(title='IS DATA OK', message=f'The Details entered are \n Website: '
                                                                        f'{website} \n Username-Email: '
                                                                        f'{email_username} \n Password: '
                                                                        f'{password}')
        if is_data_ok:
            try:
                with open('data.json', 'r') as data_file:
                    temp_data = json.load(fp=data_file)
            except FileNotFoundError:
                with open('data.json', "w") as data_file:
                    json.dump(obj=new_data, fp=data_file, indent=4)
            else:
                temp_data.update(new_data)
                with open('data.json', 'w') as data_file:
                    json.dump(obj=temp_data, fp=data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        else:
            pass
    else:
        messagebox.showinfo(title='OOPS', message='Please don\'t leave any field empty')


def check_user_data():
    if len(website) > 0 and len(email_username) > 0 and len(password) > 0:
        return True
    else:
        return False


# ---------------------------- SEARCH WEBSITE TO GET IT DETAILS FUNCTIONALITIES ------------------------------- #

def get_website_detail():
    website_value = website_entry.get()
    if len(website_value) <= 0:
        messagebox.showinfo(title='Website input field cannot be empty',
                            message='Please type the name of website you wanna search before you hit this button')
    else:
        try:
            with open('data.json', 'r') as data_file:
                temp_data = json.load(fp=data_file)
                website_details = temp_data[website_value]
        except FileNotFoundError:
            messagebox.showinfo(title='No Website added yet',
                                message='You haven\'t add any website yet, please add it and try again')
        except KeyError:
            messagebox.showinfo(title='Website not found',
                                message='The website you try to search has not been added, please add it & try again')
        else:
            messagebox.showinfo(title=f'{website_value}',
                                message=f'Email: {website_details["email"]} \nPassword: {website_details["password"]}')
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

logo_cv = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
logo_cv.create_image(100, 100, image=logo_image)
logo_cv.grid(row=0, column=1)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

search_btn = Button(text='Search', width=13, command=get_website_detail)
search_btn.grid(row=1, column=2)

email_Username_label = Label(text='Email/Username:')
email_Username_label.grid(column=0, row=2)

password_label = Label(text='Password')
password_label.grid(column=0, row=3)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_Username_entry = Entry(width=21)
email_Username_entry.grid(column=1, row=2, columnspan=2)
email_Username_entry.insert(0, 'mayheptad@ons.com')

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

gen_pass_btn = Button(text='Generate Password', command=populate_password)
gen_pass_btn.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=add_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
