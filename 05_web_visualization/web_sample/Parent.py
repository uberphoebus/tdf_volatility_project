# module name : Parent.py
#pclass extends ppclass1, ppclass2, ppclass3
from pkg.Other import oclass

class pclass(oclass): # extends ppclass :
    def __init__(self, prm):  # pclass()
        print("init call", prm)

p = pclass(4)
p.myPrint()

#p.add()

'''
    def add(self):  #instance method
        print("self add func call")

    def add(self):  #instance method
        print("overloading ...self add func call")

    def add2():     #class method
        print("add func call")

p = pclass()
p.add()
'''
#pclass.add2()