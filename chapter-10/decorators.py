def check_hello(func):
    def check_authorization(*args, **kwargs):
        print("check hello")
        return func(*args, **kwargs)
    return check_authorization

@check_hello
def hello_world(arg1=10, arg2=10):
    print("hello world")
    print(arg1*arg2)

# @check_hello
def display_price():
    print(f" price : 100")


hello_world()
display_price()