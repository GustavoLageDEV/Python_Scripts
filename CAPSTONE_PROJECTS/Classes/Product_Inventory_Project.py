#!/usr/bin/env python
# coding: utf-8

# **Product Inventory Project** - Create an application which manages an inventory of products. Create a product class which has a price, id, and quantity on hand. Then create an *inventory* class which keeps track of various products and can sum up the inventory value. 
# [[Drhealsgood (Python)]](https://github.com/Drhealsgood/miniprojects/blob/master/class_projects/product_inventory/product_inventory.py) 

class Product():

    def __init__(self,name,price,quantity=0):

        self.name = name.capitalize()
        self.price = price
        self.quantity = quantity
        self.value = round(quantity*price,2)
        self.id = 0

    def change_price(self,new_price):
        self.price = new_price
        self.value = round(self.quantity*self.price,2)

    def add_quantity(self,qtd):
        self.quantity += qtd
        self.value = round(self.quantity*self.price,2)

    def remove_quantity(self,qtd):
        self.quantity -= qtd
        self.value = round(self.quantity*self.price,2)

    def __str__(self):
        
        return self.name.capitalize()

class Inventory():

    def __init__(self):

        self.all_products = set() # PRODUCTS OBJECTS 

    def find_product(self,id): # FUNCTION TO FIND A PRODUCT BY ID.

        for product in self.all_products:
            if product.id == id:
                return product

    def add_product(self,input):

        if type(input) == Product: # CHECK IF INPUT IS A PRODUCT OBJECT
            
            for product in self.all_products: # PASSING THROUGH ALL PRODUCTS IN STOCK
                if input.name == product.name:# CHECK IF PRODUCT IS ALREADY REGISTERED IN
                    product.add_quantity(input.quantity)# IF YES ADD QUANTITY
                    print(f"+ {input.quantity} {input.name} to stock.")
                    break
                    
            else: # IF NO, ADDS PRODUCT TO IT
                self.all_products.add(input)
                input.id = len(self.all_products)
                print(f"Product added to stock: ID: {input.id} Name: {input.name} Price: {input.price} Quantity: {input.quantity}")
                
        elif type(input) == set or type(input) == list:
            for new_product in input:
                if type(new_product) == Product: # CHECK IF INPUT IS A PRODUCT OBJECT
            
                    for inv_product in self.all_products: # PASSING THROUGH ALL PRODUCTS IN STOCK
                        if new_product.name == inv_product.name:# CHECK IF PRODUCT IS ALREADY REGISTERED IN
                            inv_product.add_quantity(new_product.quantity) # IF YES ADD QUANTITY
                            print(f"+ {new_product.quantity} {new_product.name} to stock.")
                            break
                        else:
                            continue
                    
                    else: # IF NO, ADDS PRODUCT TO IT
                        self.all_products.add(new_product)
                        new_product.id = len(self.all_products)
                        print(f"Product added to stock: ID: {new_product.id} Name: {new_product.name} Price: {new_product.price} Quantity: {new_product.quantity}")
                else:  
                    print("The input did not contain Products Objects. ")

    def total_value(self):
        sum = 0
        for product in self.all_products:

            sum += product.value
        
        return sum

    def __str__(self):
        print("\n")

        for id in range(1,len(myinventory.all_products)+1):
            p = myinventory.find_product(id)
            print(f"ID:{p.id} Product: {p.name} Price: {p.price} Quantity: {p.quantity} Value: {p.value}")
            # ,p.id,p.price,p.quantity, p.total_value

        return f"\nIventory's total value: {self.total_value()}"

if __name__ == "__main__":

    myinventory = Inventory()
    
    arroz = Product("Arroz",7.99,350)
    feijao = Product("feijao",9.99,120)
    farinha = Product("farinha",6.99,300)
    
    carne = Product("carne",24.99,200)
    alface = Product("alface",5.99,500)
    arroz1 = Product("Arroz",7.99,30)
    
    novos_produtos1 = [arroz,feijao,farinha]
    novos_produtos2 = [carne,alface,arroz1]

    myinventory.add_product(novos_produtos1)
    myinventory.add_product(novos_produtos2)

    print(myinventory)