brunch_food = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
               'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

early_bird_food = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
                   'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50,
                   'coffee': 1.50, 'espresso': 3.00, }

dinner_food = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00,
               'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}

kids_food = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}

franchise = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}


class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "{a} foods are available from {b} till {c}".format(a=self.name, b=self.start_time, c=self.end_time)

    def calculate_bill(self, purchased_items):
        total = 0
        for i in purchased_items:
            total = total + self.items[i]
        return total


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr(self):
        return "The restaurant is located at{d}".format(d=self.address)

    def available_menus(self, time):
        avail = []
        for i in self.menus:
            if i.start_time <= time <= i.end_time:
                avail.append(i)
        return avail


class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


brunch = Menu("Brunch", brunch_food, 1200, 1400)
early = Menu("Early Bird", early_bird_food, 800, 1000)
dinner = Menu("Dinner", dinner_food, 1700, 2100)
kid = Menu("Kids", kids_food, 800, 2100)
print(brunch, early, dinner, kid)

print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

flagship_store = Franchise("1232 West End Road", [brunch, early, dinner, kid])
new_installment = Franchise("12 East Mulberry Street", [brunch, early, dinner, kid])
print(flagship_store.available_menus(1200))
print(flagship_store.available_menus(1800))

basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
print(basta)

areaps_menus = Menu("Franchise", franchise, 1000, 2000)
print(areaps_menus)
areaps_place = Franchise("189 Fitzgerald Avenue", [brunch, early, dinner, kid])
arepa = Business("Take a' Arepa", [areaps_place])
