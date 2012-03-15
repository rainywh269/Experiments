import sys

def do_something():
     frame = sys._getframe()
     caller = frame.f_back
     print caller.f_locals.get("A")
     #print globals().get("A")
 
def test():
    class A:
        pass
    print A
    do_something()

test()
