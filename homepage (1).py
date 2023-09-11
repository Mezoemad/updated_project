import categories as ct
import tkinter as tk
from tkinter import ttk
class home:
    def __init__(self):
        self.home_page = tk.Tk()
        self.home_page.geometry('1000x1000')
        self.home_page.title('home page')
        label = tk.Label(self.home_page,text="welcome to SIC shopping app", font=("Arial", 30))
        label.pack(padx=35, pady=35)
        self.options = ["appliances", "electronics", "fashion", "books", "sports"]
        self.selected_option = tk.StringVar()
        self.dropdown = ttk.Combobox(self.home_page, textvariable=self.selected_option, values=self.options)
        self.dropdown.pack(pady=5)
        self.selected_option.set(self.options[0])
        self.dropdown.bind("<<ComboboxSelected>>", self.on_dropdown_change)
        self.home_page.mainloop()
    def on_dropdown_change(self , event):
        selected_value = self.selected_option.get()
        self.home_page.destroy()
        ct.category(selected_value)
if __name__ == '__main__':
    home()