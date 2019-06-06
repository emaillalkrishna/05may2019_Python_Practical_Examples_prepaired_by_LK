# # # Question 10 : String
# # # Write a python program to accept the string from a user and
# # #      1. check that the string is alphanumeric or not
# # #      2. If it is alphanumeric check that it contains only alphabets or digits.
# # #      3. If it is only alphabets, check that all the alphabets are in upper case or in lower case or in mixed case

user_input_string = input("Provide the  user input in the form of string  : ")

# if user_input_string.isalnum() == True:
#     print(" User input " + user_input_string + " is an alphanumeric value")
#
#     if user_input_string.isalpha() == True:
#         print(" User input " + user_input_string + " contains only alphabetical letters")
#
#         if user_input_string.isupper():
#             print(
#                 " User input " + user_input_string + " contains only alphabetical letters and those are in upper case")
#         elif user_input_string.islower():
#             print(
#                 " User input " + user_input_string + " contains only alphabetical letters and those are in lower case")
#         else:
#             print(
#                 " User input " + user_input_string + " contains only alphabetical letters and those are in mixed case")
#
#     elif user_input_string.isnumeric() == True:
#         print(" User input " + user_input_string + " contains only numerical numbers")
