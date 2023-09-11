import json
import tkinter as tk
from tkinter import ttk
# import homepage as hp
class item():
    def __init__(self, name, price, model_year, brand, category):
        self.name = name
        self.price = price
        self.model_year = model_year
        self.brand = brand
        self.category = category
    def listsorted(self):
        file_data = []
        self.item1 = {"name": self.name, "price": self.price, "model_year": self.model_year, "brand": self.brand,
                      "category": self.category}
        with open("data_base .json", "r") as file:
            file_data = json.load(file)
        file_data.append(self.item1)
        with open("data_base.json", "w") as file:
            json.dump(file_data, file, indent=2)
electronics1 = (item("washing machine", 2000, 2022, "Toshiba", "electronics"))
electronics1.listsorted()
electronics2 = (item("refrigetator", 3000, 2020, "Fresh", "electronics"))
electronics2.listsorted()
electronics3 = (item("TV", 4000, 2021, "Samsung", "electronics"))
electronics3.listsorted()
appliances1 = (item("hand blender", 1000, 2018, "Fresh", "appliances"))
appliances1.listsorted()
appliances2 = (item("air frier", 5000, 2023, "Philips", "appliances"))
appliances2.listsorted()
appliances3 = (item("pan", 100, 2023, "tefal", "appliances"))
appliances3.listsorted()
fashion1 = (item("shirt", 150, 2021, "zara", "fashion"))
fashion1.listsorted()
fashion2 = (item("shoes", 200, 2023, "adidas", "fashion"))
fashion2.listsorted()
fashion3 = (item("pants", 250, 2020, "H&M", "fashion"))
fashion3.listsorted()
books1 = (item("story", 50, 2023, "Alshrouq", "books"))
books1.listsorted()
books2 = (item("science_book", 100, 2022, "Dawen", "books"))
books2.listsorted()
books3 = ((item("novel", 150, 2016, "عصير الكتب", "books")))
books3.listsorted()
sports1 = (item("racket", 60, 2022, "ssss", "sports"))
sports1.listsorted()
sports2 = (item("rope", 30, 2021, "hhhh", "sports"))
sports2.listsorted()
sports3 = (item("karate suit", 200, 2020, "uuuuuu", "sports"))
sports3.listsorted()
class category():
    def __init__(self, name):
        self.root = tk.Tk()
        self.root.geometry("600x6000")
        self.name = name
        Label = tk.Label(self.root, text=name, font=("Arial", 25))
        Label.pack(padx=20, pady=25)
        self.button1 = tk.Button(self.root, text="sort", font=("Arial", 18),)
        self.button1.place(x=380, y=80)
        self.options = ["price", "model_year", "brand", "name"]
        self.selected_option = tk.StringVar()
        self.dropdown = ttk.Combobox(self.root, textvariable=self.selected_option, values=self.options)
        self.dropdown.pack(pady=15)
        self.selected_option.set(self.options[0])
        self.search = tk.Entry(font=("Arial, 18"), width=8)
        self.search.pack(padx=10, pady=10)
        self.button2 = tk.Button(self.root, text="search", font=("Arial", 18), command=self.searching)
        self.button2.place(x=100, y=80)
        if self.searcing():
            self.labelsearching=tk.Label(text=self.searcing(),height=3, width=9)
            self.labelsearching.pack(padx=10,pady=10)
        elif self.sort1() and not self.searcing():
            self.labelsorting=tk.Label(text=self.sort1(),height=3, width=9)
            self.labelsorting.pack(pady=10,padx=10)
        else:
            with open("data_base.json", "r") as file:
                file_data = json.load(file)
            for item in file_data:
                if item['category'] == name:
                    self.text_box1 = tk.Label(self.root, height=3, width=5, text=item['name'])
                    self.text_box1.pack(padx=10, pady=5)
                    self.text_box2 = tk.Label(self.root, height=3, width=5, text=item['price'])
                    self.text_box2.pack(padx=10, pady=15)
                    self.text_box3 = tk.Label(self.root, height=3, width=5, text=item['model_year'])
                    self.text_box3.pack(padx=10, pady=15)
                    self.text_box4 = tk.Label(self.root, height=3, width=5, text=item['brand'])
                    self.text_box4.pack(padx=10, pady=15)
        self.root.mainloop()
    def sort1(self):
        with open("data_base.json", "r") as file:
            file_data = json.load(file)
        n = len(file_data)
        for i in range(n - 1):
            for j in range(i, 0, -1):
                if file_data[j][self.selected_option] < file_data[j - 1][self.selected_option]:
                    file_data[j - 1], file_data[j] = file_data[j], file_data[j - 1]
        return file_data
    def binary_search(self, name, file_data):
        left = 0
        right = len(file_data) - 1
        steps = 0
        while left <= right:
            mid = (left + right) // 2
            steps += 1
            if name == file_data[mid]["name"]:
                return file_data[mid]
            elif name > file_data[mid]["name"]:
                left = mid + 1
            elif name < file_data[mid]["name"]:
                right = mid - 1
    def searcing(self):
        with open("data_base.json", "r") as file:
            file_data = json.load(file)
        self.sort1()
        item_searched = self.binary_search(self.search.get(), file_data)
        return item_searched
    # def search_item(self):
    #     with open("data_base.json", "r") as file:
    #         file_data = json.load(file)
    #     selected_item = self.search.get()
    #     for item in file_data:
    #         if selected_item == item[]



