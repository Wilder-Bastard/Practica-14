import tkinter as tk
from tkinter import messagebox


class IceCreamStand:
    def __init__(self, name):
        self.name = name
        self.flavors = []
        self.stick = []
        self.soft = []

    def add_flavor(self, flavor):
        if flavor and flavor not in self.flavors:
            self.flavors.append(flavor)
            return True
        return False

    def get_flavors_text(self):
        if not self.flavors:
            return "Список пуст"
        return ", ".join(self.flavors)

cafe = IceCreamStand("Сладкий рожок")

window = tk.Tk()
window.title("Мороженное у Ашота")
window.geometry("400x300")

tk.Label(window, text="Мороженное у Ашота", font=("Arial", 16)).pack(pady=10)

entry = tk.Entry(window, width=30)
entry.pack(pady=5)

def add():
    flavor = entry.get()
    if cafe.add_flavor(flavor):
        label_result.config(text=f"Сорта: {cafe.get_flavors_text()}")
        entry.delete(0, tk.END)
        messagebox.showinfo("Успех", f"Добавлен {flavor}")
    else:
        messagebox.showwarning("Ошибка", "Такой сорт уже есть или поле пустое")


tk.Button(window, text="Добавить сорт", command=add).pack(pady=5)

label_result = tk.Label(window, text="Сорта: Список пуст", font=("Arial", 12))
label_result.pack(pady=20)

tk.Button(window, text="Выход", command=window.quit, bg="red", fg="white").pack(pady=10)

window.mainloop()