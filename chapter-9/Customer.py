class Customer():
    country = 'Indonesia'

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def multiply_age(self):
        return self.age*2

class SuperCustomer(Customer):
    def __init__(self, name, age, address, expire_date):
        Customer.__init__(self, name, age, address)
        self.expire_date = expire_date



sc = SuperCustomer("Joe", 99, "1600 Pensylvania Ave", "11/02/2025")
print(sc.multiply_age())


# customer = Customer("Joe", 56, "1600 Pensylvania Ave")
#
# print(customer.multiply_age())

