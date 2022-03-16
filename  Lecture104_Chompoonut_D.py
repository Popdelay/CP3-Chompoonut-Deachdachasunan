class Customer:
    name = ""
    lastName = ""
    Product = ""
    age = 0

    def addCart(self):
        print("Add",self.Product , "to cart" ,self.name , self.lastName)

customer1 = Customer()
customer1.name = "Chompoonut"
customer1.lastName= "D."
customer1.Product="Book"


customer2 = Customer()
customer2.name = "Maithai"
customer2.lastName= "S."
customer2.Product="Water"

customer3 = Customer()
customer3.name = "Chompoonut"
customer3.lastName= "D."
customer3.Product="Banana"

customer4 = Customer()
customer4.name = "Chompoonut"
customer4.lastName= "D."
customer4.Product="Pen"

customer1.addCart()
customer2.addCart()
customer3.addCart()
customer4.addCart()