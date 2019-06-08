# # # # Python program to print
# # #                           The first half from left to right
# # #                           The second half from right to left


# # # -----------------------------------Method 1 --------------------------------
my_list = [5, 4, 6, 2, 1, 3, 8, 9, 7]
my_list_length = len(my_list)

# printing first half in ascending order
print("first half in ascending order")
i = 0
while i < (my_list_length / 2):
    print(my_list[i])
    i = i + 1


# printing second half in descending order
print("second half in descending order")
j = my_list_length - 1
while j >= my_list_length / 2:
    print(my_list[j])
    j = j - 1


# # # --------------------------Same with in a function
# def printOrder(my_list, n):
#     # sorting the array
#     my_list.sort()
#
#     # printing first half in ascending order
#     print("Printing the first half from left to right")
#     i = 0
#     while (i < (n / 2)):
#         print(my_list[i])
#         i = i + 1
#
#     # printing second half in descending  order
#     print("Printing the second half from right to left")
#     j = n - 1
#     while j >= n / 2:
#         print(my_list[j])
#         j = j - 1
#
#
# my_list = [5, 4, 6, 2, 1, 3, 8, 9, 7]
# n = len(my_list)
# printOrder(my_list, n)



# # # ----------------------------------------Method 2 ------------------------------------------
# def printOrder(arr, n):
#    # sorting the array
#    arr.sort()
#
#    # printing first half in ascending order
#    for i in range(n // 2):
#        print(arr[i], end=" ")
#
#    # printing second half in descending order
#    for j in range(n - 1, n // 2 - 1, -1):
#        print(arr[j], end=" ")
#
# # Driver code
# if __name__ == "__main__":
#    arr = [5, 4, 6, 2, 1, 3, 8, 9]
#    n = len(arr)
#    printOrder(arr, n)





















