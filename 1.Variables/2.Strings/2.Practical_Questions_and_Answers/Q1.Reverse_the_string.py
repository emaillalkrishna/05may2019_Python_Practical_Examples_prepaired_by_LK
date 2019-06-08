# # # -------------------------------Question 2 : String → Reverse------------------------------------------------

# # # -----------------------------------Method 1 : Using Slicing-------------------------------------------------

# my_input = input("Type the string for reversing : ")
# print(my_input [ :  : -1 ])

# # # -----------------------------------Method 2 : Using While loop-----------------------------------------------
# my_input = input("Type the string for reversing : ")
# my_string = ""
#
# i = len(my_input) - 1
# while i >= 0:
#     my_string = my_string + my_input[i]
#     i = i - 1
# print(my_string)
