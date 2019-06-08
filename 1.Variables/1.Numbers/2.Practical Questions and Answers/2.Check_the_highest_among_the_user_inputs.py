# # # # Question 2 : Numbers → Check the highest among the user inputs
#
# # # # -----------------------------------------Method 1--------------------------------------------
# num1 = float(input("Please enter the First number:  "))
# num2 = float(input("Please enter the Second number: "))
# num3 = float(input("Please enter the Third number:  "))
#
# if (num1 > num2) and (num1 > num3):
#     print("The largest number among the three numbers ", num1)
#
# elif (num2 > num1) and (num2 > num3):
#     print("The largest number among the three numbers ", num2)
#
# elif (num3 > num1) and (num3 > num2):
#     print("The largest number among the three numbers ", num3)
#
# else:
#     print("All the three numbers are equal")
#
# # # # ----------------------------------------Method 2---------------------------------------------
# num1 = float(input(" Please Enter the First Value a: "))
# num2 = float(input(" Please Enter the Second Value b: "))
#
# if (num1 > num2):
#     print("{0} is Greater than {1}".format(num1, num2))
#
# elif (num2 > num1):
#     print("{1} is Greater than {0}".format(a, b))
#
# else:
#     print("Both a and b are Equal")
