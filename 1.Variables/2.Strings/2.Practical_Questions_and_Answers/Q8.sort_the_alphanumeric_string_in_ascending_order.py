# # # Question 8 : String → Sorting the alphanumeric string in ascending order

# # # ------------------------------My best method is the below one --------------
# my_string = input("Enter value: ")
#
# my_alphabetical_string = ""
# my_numerical_string = ""
# my_final_string = ""
#
# for i in my_string:
#
#     if i.isalpha():
#         my_alphabetical_string = my_alphabetical_string + i
#     else:
#         my_numerical_string = my_numerical_string + i
#
# my_alphabetical_string_sorted_to_list_form = sorted(my_alphabetical_string)
# my_numerical_string_sorted_to_list_form = sorted(my_numerical_string)
#
# my_sorted_final_list = my_alphabetical_string_sorted_to_list_form + my_numerical_string_sorted_to_list_form
#
# for i in my_sorted_final_list:
#     my_final_string = my_final_string + i
# print(my_final_string)



# # # -------------------------------------------
# my_string = input("Enter value: ")
#
# my_alphabetical_string = ""
# my_numerical_string = ""
# my_final_string = ""
#
# for i in my_string:
#
#     if i.isalpha():
#         my_alphabetical_string = my_alphabetical_string + i
#     else:
#         my_numerical_string = my_numerical_string + i
#
# for i in sorted(my_alphabetical_string):
#     my_final_string = my_final_string + i
#
# for i in sorted(my_numerical_string):
#     my_final_string = my_final_string + i
#
# print(my_final_string)


