import tkinter as tk
import json
import gui_login
class users:
    def __init__(self, Register):
        self.Register = Register
        self.name = tk.Label(self.Register, text='Name', font=('SamsungOne 400', 9))
        self.name.pack(padx=1, pady=1)
        self.entry_name = tk.Entry()
        self.entry_name.pack()
        self.phone = tk.Label(self.Register, text='phone', font=('SamsungOne 400', 9))
        self.phone.pack(padx=1, pady=1)
        self.entry_phone = tk.Entry()
        self.entry_phone.pack()
        self.mail = tk.Label(self.Register, text='mail', font=('SamsungOne 400', 9))
        self.mail.pack(padx=1, pady=1)
        self.entry_mail = tk.Entry()
        self.entry_mail.pack()

        self.gender = tk.Label(self.Register, text='gender', font=('SamsungOne 400', 9))
        self.gender.pack(padx=1, pady=1)
        self.entry_gender = tk.Entry()
        self.entry_gender.pack()

        self.age = tk.Label(self.Register, text='age', font=('SamsungOne 400', 9))
        self.age.pack(padx=1, pady=1)
        self.entry_age = tk.Entry()
        self.entry_age.pack()

        self.governorate = tk.Label(self.Register, text='governorate', font=('SamsungOne 400', 9))
        self.governorate.pack(padx=1, pady=1)
        self.entry_governorate = tk.Entry()
        self.entry_governorate.pack()

        self.ID = tk.Label(self.Register, text='ID', font=('SamsungOne 400', 9))
        self.ID.pack(padx=1, pady=1)
        self.entry_ID = tk.Entry()
        self.entry_ID.pack()
        self.password = tk.Label(self.Register, text='password', font=('SamsungOne 400', 9))
        self.password.pack(padx=1, pady=1)
        self.entry_password = tk.Entry()
        self.entry_password.pack()
        self.reg = tk.Button(self.Register, text='Register', font=('Times New Roman', 15), command=self.addjson)
        self.reg.pack(padx=50, pady=50)
        self.Register.mainloop
    def addjson(self):
        user = {"id": self.entry_ID.get(), "name": self.entry_name.get(), "password": self.entry_password.get(),
                "phone": self.entry_phone.get(), "mail": self.entry_mail.get(), "gender": self.entry_gender.get(),
                "age": self.entry_age.get(), "governorate": self.entry_governorate.get()}
        with open("data.json", "r") as file:
            file_data = json.load(file)
        file_data.append(user)
        with open("data.json", "w") as file:
            json.dump(file_data, file, indent=2)
class Register:
    def __init__(self):
        self.Register = tk.Tk()
        self.Register.geometry('600x600')
        self.Register.title('Register')
        def open_login_page():
            self.Register.destroy()
            gui_login.login()
        button = tk.Button(text='Sign in', command=open_login_page)
        button.place(x=260, y=500, width=80)
        users(self.Register)
        self.Register.mainloop()
if __name__ == '__main__':
    Register()
