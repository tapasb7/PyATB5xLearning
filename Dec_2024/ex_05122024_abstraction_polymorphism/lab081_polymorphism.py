#procedural method overload is not supported in python

class Cal:

    def sum(self,*args): #*args is multiple arguments
        for i in args:
            print(i)

obj_ref = Cal()
obj_ref.sum(1,3,5)