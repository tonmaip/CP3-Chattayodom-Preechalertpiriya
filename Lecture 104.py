class Customer:
    name = ""
    lastName = ""
    age = 0

    def adCart(self):
        print("AdCart product to", self.name, self.lastName, "'s Cart")

customer1 = Customer()
customer1.name = "Tonmai"
customer1.lastName = "Preech"
customer1.adCart()

customer2 = Customer()
customer2.name = "kaijeaw"
customer2.lastName = "junocha"
customer2.adCart()


customer3 = Customer()
customer3.name = "paopay"
customer3.lastName = "junohshi"
customer3.adCart()