# *args - Tuple take unlimited arguments

# def add(*args):
#     sum = 0
#     for i in args[0]:
#         sum += i
#     return f"sum: {sum}"
   
# list = [150,100]
# print(add(list))


# **kwargs - dictionary takes unlimited arguments
class Car:

    def __init__(self, **kw):
        self.brand = kw["brand"]
        self.model = kw["model"]
        self.seats = kw.get("seats")
my_car = Car(brand = "MG", model = "GT-45")
print(my_car.model)

# we didnt initialize seats if print my_Car.seats it returns None as you used get()
print(my_car.seats)

# using both *args and **kwargs

def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)
