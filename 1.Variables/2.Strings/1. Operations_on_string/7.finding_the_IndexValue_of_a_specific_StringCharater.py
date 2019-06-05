# var = "qspiders"
# print(var.index("p"))             # Ans: 2
#
# var = "qspiders"
# print(var.find("p"))              # Ans : 2
#
## Difference between index() method and find() is
## If the characters is which we provided inside the method is not available in the  string
## --> then the index() method will thrown an error message
## --> then the find() method will not thrown any error message, instead it will show the result as -1
#
#
# var = "qspiders"
# print(var.index("z"))             # Ans: ValueError: substring not found
#
# var = "qspiders"
# print(var.find("z"))              # Ans : -1
