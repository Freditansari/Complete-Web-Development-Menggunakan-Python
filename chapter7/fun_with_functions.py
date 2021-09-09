# def my_function(*nama):
#     print(nama[2])
#
# # KWargs arbritary keywords arguments
# my_function('Jon', 'Joe', 'Sue')

def my_function(**customer):
    print('last name of the customer : ' + customer['lname'])

# KWargs arbritary keywords arguments
my_function(fname= "Mike", lname='rotch')

