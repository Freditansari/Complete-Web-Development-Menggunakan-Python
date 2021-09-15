def check_hello(func):
    print("check Hello")
    func()

@check_hello
def hello_world():
    print("hello world")

# check_hello(hello_world)

