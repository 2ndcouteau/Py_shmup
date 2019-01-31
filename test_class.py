#!/usr/bin/python3
# _*_ coding: Utf-8 -*


class Toto:
	arg1 = "salut"

	def __init__(self, arg2):
		self.arg2 = arg2
		self.arg3 = "Bonjour"

		self.__arg4 = arg2 + " is private"
		print ("init arg4 == " + self.__arg4)



obj1 = Toto("OBJ1")
obj2 = Toto("OBJ2")

print ("obj1.arg1== " + obj1.arg1)
print ("obj1.arg2== " + obj1.arg2)
print ("obj1.arg3== " + obj1.arg3)

obj1.arg1 = "bonsoir"
print ("obj1.arg1== " + obj1.arg1)
print ("obj2.arg1== " + obj2.arg1)


obj2.abcd = "efgh"
print (obj2.abcd.upper())
