# # # Question 7 : String → Sorting a string in ascending order

my_string = input("Enter value: ")
my_sorted_list = sorted(my_string)
my_sorted_string = ""

for i in my_sorted_list:
    my_sorted_string = my_sorted_string + i


print(my_sorted_string)
