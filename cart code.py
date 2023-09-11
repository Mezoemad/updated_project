import tkinter as tk
import json
from tkinter import ttk
from tkinter import messagebox



class cart:
    def __init__(self):
        self.cart = tk.Tk()
        self.cart.geometry('1000x1000')
        self.cart.title('cart')
        self.label = tk.Label(self.cart, text='your cart ', font=('om-gel', 50))
        self.label.pack(padx=100, pady=50)
        self.name = tk.Label(self.cart, text='Name', font=('SamsungOne 400', 9))
        self.name.pack(padx=1, pady=1)
        self.entry_name = tk.Entry()
        self.entry_name.pack()
        self.price = tk.Label(self.cart, text='price', font=('SamsungOne 400', 9))
        self.price.pack(padx=1, pady=1)
        self.entry_price = tk.Entry()
        self.entry_price.pack()
        self.model = tk.Label(self.cart, text='model_year', font=('SamsungOne 400', 9))
        self.model.pack(padx=1, pady=1)
        self.entry_model = tk.Entry()
        self.entry_model.pack()
        self.brand = tk.Label(self.cart, text='brand', font=('SamsungOne 400', 9))
        self.brand.pack(padx=1, pady=1)
        self.entry_brand = tk.Entry()
        self.entry_brand.pack()
        self.options = ["cairo", "alex", "aswan"]
        self.selected_option = tk.StringVar()
        self.dropdown = ttk.Combobox(self.cart, textvariable=self.selected_option, values=self.options)
        self.dropdown.pack(pady=5)
        self.selected_option.set(self.options[0])
        self.dropdown.bind("<<ComboboxSelected>>", self.addprice)
        button1 = tk.Button(self.cart, text="total price", command=self.show_total)
        button1.pack()
        self.cart.mainloop()

    def addprice(self):
        total = 0
        l2 = {"cairo": 50, "alex": 30, "aswan": 100}
        total += l2[self.selected_option.get()]
        with open("data_base.json", "r") as file:
            file_data = json.load(file)
        for item in file_data:
            if item['name'] == self.entry_name.get() and item["price"] == self.entry_price.get():
                if item["brand"] == self.entry_brand.get() and item["model_year"] == self.entry_model.get():
                    total += item["price"]
        messagebox.showinfo("Total price", f"price = {self.addprice}")


    def show_total(self):
        total = messagebox.showinfo("Total price", f"price = {self.addprice}")
        return total


cart1 = cart()
