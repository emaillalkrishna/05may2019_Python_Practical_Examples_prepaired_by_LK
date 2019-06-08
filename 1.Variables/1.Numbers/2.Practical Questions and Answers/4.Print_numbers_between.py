# # # Question 4 : Range function → Print all odd numbers in between 1 to 10



# # # The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers,
#      range( starting from 0 by default,  and ends at a specified number, and increments by 1 (by default)   )
#
# for i in range(6):
#   print(i)                         # Ans : Note that range(6) is not the values of 0 to 6, but the values 0 to 5.


# # # #               ---------------------------------------------------------------------------
# for i in range(2, 6):
#   print(i)
#
# # Ans : The range() function defaults to 0 as a starting value,
# #       however it is possible to specify the starting value by adding a parameter: range(2, 6),
# #       which means values from 2 to 6 (but not including 6):
#
# # # #               ---------------------------------------------------------------------------
# for i in range(2, 30, 3):
#   print(i)
#
# # Ans : The range() function defaults to increment the sequence by 1,
# #       however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
#
#
# # # #               ---------------------------------------------------------------------------
#
# # # # Write a python program to print all the even numbers between one to hundred. (Hundred included)
# for i in range(2, 101, 2):
#     print(i)

#
# # # # Write a python program to print all even numbers in between 1 to 10
# for i in range(2, 11, 2):
#     print(i)

# # # # Write a python program to print all odd numbers in between 1 to 10
# for i in range(1, 10, 2):
#     print(i)
