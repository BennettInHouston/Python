from flask import Flask

app = flask(__name__)
class Parent:

    def altered (self):
        print ("PARENT altered ()")

class Child (Parent):

    def altered (self):
        print ("CHILD before PARENT altered ()")
        super (Child, self).altered ()
        print ("CHILD after PARENT altered ()")

dad = Parent ()
son = Child ()

dad.altered ()
son.altered ()
