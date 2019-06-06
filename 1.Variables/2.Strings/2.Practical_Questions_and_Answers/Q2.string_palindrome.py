# # # Question 3 : String → Palindrome

# # # --------------------------------------------- Method 1 ---------------------------------------------------------
# my_string = input("Enter string value:")
# my_rev_string = my_string[::-1]
#
# if (my_string == my_rev_string):
#     print("String provided is a palindrome")
# else:
#     print("String provided is not a  palindrome")


# # # --------------------------------------------- Method 2 ---------------------------------------------------------

# my_string = input("Enter string value:")
# my_rev_string = ""
#
# i = len(my_string) - 1
# while i >= 0:
#     my_rev_string = my_rev_string + my_string[i]
#     i = i - 1
# print(my_rev_string)
#
# if (my_string == my_rev_string):
#     print("String provided is a palindrome")
# else:
#     print("String provided is not a  palindrome")

# # # Note
# # # The above two method can be used when the uses provide the string in the same case
# # # that means when the user give the input as "malayalam" then program identify that as a palindrome.
# # # But when the user give the input as "Malayalam" then it will identify that a non palindrome
# # # It is because according to the program the uppercase "M" and lower case "m" are two different characters.


# # Note:It is not necessary that we have to use the casefold() method, we can even use upper() or lower() method.
# # my_str_all_upper_case = my_str.upper()
# # my_str_all_lower_case = my_str.lower()


# my_string = input("Enter string value:")
# my_string_casefolded = my_string.casefold()
# my_rev_string_casefolded = my_string_casefolded[::-1]
#
# if my_string_casefolded == my_rev_string_casefolded:
#     print("String provided by the user is palindrome")
# else:
#     print("String provided by the user not palindrome")

# # # ----------------------------------------------------------------------

# my_string = input("Enter string value:")
# my_string_casefolded = my_string.casefold()
# my_str_casefolded_reversed = reversed(my_string_casefolded)
#
# if list(my_string_casefolded) == list(my_str_casefolded_reversed):
#     print("String provided by the user is palindrome")
# else:
#     print("String provided by the user not palindrome")


