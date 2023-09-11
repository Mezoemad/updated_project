import tkinter as tk
from tkinter import messagebox
import project_register
from homepage import home
import json

class login:

    def __init__(self):
        self.gui = tk.Tk()


        def login():
            self.username = input_username.get()
            self.password = input_password.get()
            with open("data.json", "r") as file:
                file_data = json.load(file)
            if self.username == "admin@gmail.com" and self.password == "admin123":
                messagebox.showinfo("Login Successful", "Welcome admin !")
                home()
            # elif self.username in file_data:
            #     if file_data[self.username] == file_data[self.password]:
            #         messagebox.showinfo("Login Success", "Welcome user")
            else:
                for i in file_data:
                    if i['mail'] == self.username:
                        if i['password'] == self.password:
                            messagebox.showinfo("Login Success", "Welcome user")
                            home()



                messagebox.showerror("login failed", " Invalid email or password")
        self.gui.configure(bg='#333333')
        self.gui.geometry("400x400")
        title = self.gui.title("Online shopping")

        label1 = tk.Label(self.gui, text="Login page", font=('Arial', 15), bg='#333333', fg='white')
        label1.pack(padx=30, pady=30)

        label2 = tk.Label(self.gui, text="Enter your email", font=('Arial', 11), bg='#333333', fg='white')
        label2.pack(padx=30)

        input_username = tk.Entry(self.gui)
        input_username.pack()

        label3 = tk.Label(self.gui, text="Enter your password", font=('Arial', 11), bg='#333333', fg='white')
        label3.pack(padx=30)

        input_password = tk.Entry(self.gui, show="*")
        input_password.pack()

        button_login = tk.Button(text='Sign in', font=('Arial', 10), command=login)
        button_login.pack(pady=20)

        button_register = tk.Button(text='Create new account ?', font=('Arial', 10), fg='#333333', command=self.open_register_page)
        button_register.pack(pady=50)

        tk.mainloop()

    def open_register_page(self):
        self.gui.destroy()
        project_register.Register()


if __name__ == '__main__':
    login()
