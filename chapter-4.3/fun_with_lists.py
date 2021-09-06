customers=["Joe", 'Sarah', 10]

print("before : "+str(customers))


new_customer = "banana"
customers.append(new_customer)

#pop / remove
#index

# index_number = customers.index("Joe")
#
# customers.pop(index_number)

customers.remove('Sarah')

print("after : "+str(customers))