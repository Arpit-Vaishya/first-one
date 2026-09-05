class Menuitem:
   def __init__(self,name,price):
       self.name=name
       self.price=price
      
class Restaurant:
    def __init__(self,name,location):
        self.name=name
        self.location=location
        self.menu_items=[]
      
    def add_menu_item(self,menu_item): 
        self.menu_items.append(menu_item)
    def display_menu(self):
        print(f"Menu for {self.name} at {self.location}:")
        for item in self.menu_items:
            print(f"{item.name}: ${item.price}\n")

class Order:    
    def __init__(self,customer):
        self.customer=customer
        self.items=[]
        pass
    def add_item(self,item):
        self.items.append(item)
        print(f"{item.name} added to {self.customer}'s order.")
    def bill(self):
        self.total=0
        for item in self.items:
            print(f"{item.name}: ${item.price}")
            self.total+=item.price
        print(f"{self.customer}'s bill is {self.total}")

pizza=Menuitem("Pizza", 12.99)
burger=Menuitem("Burger", 8.99)
nachos=Menuitem("Nachos", 6.99)
coke=Menuitem("Coke", 1.99)
pasta=Menuitem("Pasta", 10.99)
banana=Menuitem("Banana", 0.99)
water=Menuitem("Water", 0.00)
cold_coffee=Menuitem("Cold Coffee", 3.99)
tea=Menuitem("Tea", 2.49)
cake=Menuitem("Choco Cake",9.99)
vodka=Menuitem("Vodka", 15.99)

berlin=Restaurant("Berlin Bites and Drinks", "TCET Mumbai")
berlin.add_menu_item(pizza)
berlin.add_menu_item(burger)
berlin.add_menu_item(nachos)
berlin.add_menu_item(coke)
berlin.add_menu_item(pasta)
berlin.add_menu_item(banana)
berlin.add_menu_item(water)
berlin.add_menu_item(cold_coffee)
berlin.add_menu_item(tea)
berlin.add_menu_item(cake)
berlin.add_menu_item(vodka)
berlin.display_menu()

consumer=Order("Alita one")
consumer.add_item(pizza)
consumer.add_item(coke)
consumer.add_item(nachos)
consumer.bill()


