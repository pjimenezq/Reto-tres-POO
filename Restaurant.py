class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Beverage(MenuItem):
    def __init__(self, name, price, alcohol, temperature):
        super().__init__(name, price)
        self.alcohol = alcohol
        self.temperature = temperature

class MainCourse(MenuItem):
    def __init__(self, name, price, vegetarian, spicy):
        super().__init__(name, price)
        self.vegetarian = vegetarian
        self.spicy = spicy

class Dessert(MenuItem):
    def __init__(self, name, price, peanuts, vegan):
        super().__init__(name, price)
        self.peanuts = peanuts
        self.vegan = vegan


class Order:
    def __init__(self, order_list: list=[]):
        self.order_list = order_list

    def add_items(self, new_items_list: list= []):
        x = 0
        while x<len(new_items_list):
            self.order_list.append(new_items_list[x])#The new items are added to the original order list
            x+=1
    def bill_amount(self):
        x = 0
        sum = 0 #The variable is for adding all the prices of the items that are in order_list
        while x<len(self.order_list):
            sum+=self.order_list[x].price
            x+=1
        if self.order_list.count(beer)>=3:#There is a discount for the beers: buy 3, get 1 free
            beer_count = self.order_list.count(beer)
            beer_discount = int(beer_count/3)
            sum-=(beer.price*beer_discount)

        print("The total price is $" +str(sum)) 
    
    
beer = Beverage("Beer", 10.000, "Alcoholic", "Cold" )
water = Beverage("Bottle of water", 6.500, "Non-alcoholic", "Room temperature" )
soda = Beverage("Coca-Cola", 6.000,"Non-alcoholic", "Cold" )
coffee = Beverage("Cappuccino", 6.100, "Non-alcoholic", "Hot" )
salad = MainCourse("Caesar salad", 23.000, "Non-vegetarian", "Non-spicy" )
lasagna = MainCourse("Lasagna", 25.000, "Vegetarian", "Non-spicy")
tacos = MainCourse("Chicken Tacos", 20.000, "Non-vegetarian", "Spicy")
waffle = Dessert("Nutella waffles", 15.000, "Contains peanuts", "Non-vegan" )
iceCream = Dessert("Lemon ice cream", 5.000, "Without peanuts", "Vegan" )
tiramisu = Dessert("Tiramisu", 12.000, "Without peanuts", "Non-vegan")


order = Order([waffle, salad, beer])
order.bill_amount()
order.add_items([beer, beer, lasagna, tacos ])
order.bill_amount()
