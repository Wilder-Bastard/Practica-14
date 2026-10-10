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
        print("Ресторан", self.restaurant_name, "открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, kitchen_type, rating, flavors):
        super().__init__(restaurant_name, kitchen_type, rating)
        self.flavors = flavors

    def show_flavors(self):
        print("Сорта мороженого:")
        for flavor in self.flavors:
            print("-", flavor)


ice = IceCreamStand("Хинкаль и мороженое", "грузинская", 5, ["ваниль", "шоколад", "банановое", "серобуромалиновое"])
ice.show_flavors()