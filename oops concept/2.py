class ram():
    def display(self):
        a=10
        b=20
        print(a,b)
        print(a+b)
obj=ram()
obj.display()



class person():
    print("hello darling")


class mobiles():
    print("welcome to mobile store")
    def __init__(self,ram,storage,cam,price):
        self.ram=ram
        self.storage=storage
        self.cam=cam
        self.price=price

obj=mobiles("8gb",'128gb','64mp','16,000')
print(obj.price)
        
    
