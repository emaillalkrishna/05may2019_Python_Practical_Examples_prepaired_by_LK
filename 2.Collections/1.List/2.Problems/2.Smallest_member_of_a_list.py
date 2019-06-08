# # #  List 1→ Smallest member of a list

# # # # ----------------------------Method 1: --------------------------------------------------
my_list = [1, 2, 70, 10, 50]
print(min(my_list))

# # # # ----------------------------Method 2: --------------------------------------------------

my_list = []
my_list_length = int(input('How many numbers: '))
for i in range(my_list_length):
   numbers = int(input('Enter number '))
   my_list.append(numbers)
print("Maximum element in the list is :", max(my_list))
print("Minimum element in the list is :", min(my_list))

# # # # ----------------------------Method 3: --------------------------------------------------

# my_list = [1, 2, 70, 10, 50]
# my_list.sort()
# print(my_list)
# print(my_list[0])
