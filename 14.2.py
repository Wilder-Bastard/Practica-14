class Restaurant:
    def __init__(self, restaurant_name, kitchen_type, rating=0):
        self.restaurant_name = restaurant_name
        self.kitchen_type = kitchen_type
        self.rating = rating

    def describe_restaurant(self):
        print("Название:", self.restaurant_name)
        print("Тип кухни:", self.kitchen_type)
        print("Рейтинг:", self.rating)

    def open_restaurant(self):
        print("Ресторан", self.restaurant_name, "сальто!")

    def update_rating(self, new_rating):
        self.rating = new_rating


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, kitchen_type, rating, flavors, location, work_time):
        super().__init__(restaurant_name, kitchen_type, rating)
        self.flavors = flavors
        self.location = location
        self.work_time = work_time
        self.stick_ice_cream = []
        self.soft_ice_cream = []

    def show_flavors(self):
        print("Сорта мороженого:")
        for flavor in self.flavors:
            print("-", flavor)

    def add_flavor(self, flavor):
        self.flavors.append(flavor)
        print("Добавлен сорт:", flavor)

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print("Удалён сорт:", flavor)
        else:
            print("Такого сорта нет:", flavor)

    def has_flavor(self, flavor):
        if flavor in self.flavors:
            print("Сорт", flavor, "есть в наличии")
        else:
            print("Сорта", flavor, "нет в наличии")

    def add_stick(self, flavor):
        self.stick_ice_cream.append(flavor)
        print("Мороженое на палочке добавлено:", flavor)

    def add_soft(self, flavor):
        self.soft_ice_cream.append(flavor)
        print("Мягкое мороженое добавлено:", flavor)

    def show_types(self):
        print("На палочке:", self.stick_ice_cream)
        print("Мягкое:", self.soft_ice_cream)


ice = IceCreamStand("Хинкаль и мороженое", "грузинская", 5,
                    ["ваниль", "шоколад"],
                    "Тбилиси, ул. Руставели 1", "10:00 - 22:00")

ice.show_flavors()
ice.add_flavor("банановое")
ice.remove_flavor("шоколад")
ice.has_flavor("ваниль")
ice.has_flavor("клубничное")
ice.add_stick("эскимо")
ice.add_soft("рожок")
ice.show_types()