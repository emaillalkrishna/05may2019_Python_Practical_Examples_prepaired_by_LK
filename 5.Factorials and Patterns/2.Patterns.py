#
# # # # Case 1
# for i in range(1, 4):
#    print(i)
# # # # Case 2
# for j in range(1, 4):
#    print('*')
# # # # Case 3
# for k in range(1, 4):
#    print('*', end=" ")
#
# # Case 4
# # Note :
# # # For getting an output like this we have combined both case 2 and case 3
# # #             Here end= is a keyword
# # #             First we will take a value from the outer range →
# # # #           then go to the inner range and perform the inner loop completely  →
# # # #           then come out of the inner loop and fetch another value of the outer loop,
# # # #           repeat the same till the outer loop gets complete.
#
# for i in range(1, 4):
#    for j in range(1, 4):
#        print("*", end="  ")
#    print()
#
#
# # # # Case 5
# for i in range(1, 4):
#    for j in range(1, 4):
#        print(i, end="  ")
#    print()
#
# # # # Case 6
# for i in range(1, 4):
#    for j in range(1, 4):
#        print(j, end="  ")
#    print()
#
# # # # Case 7
# n = int(input("Enter the number of rows: "))
# for i in range(1, n + 1):
#    for j in range(1, i + 1):
#        print(i, end=" ")
#    print()
#
# # # # Case 8
# n = int(input("Enter the number of rows: "))
# for i in range(1, n + 1):
#    for j in range(1, i + 1):
#        print(chr(64 + j), end=" ")
#    print()
#
#
# # # # Case 9
# n = int(input("Enter the number of rows: "))
# for i in range(1, n + 1):
#    print(" " * (n - i), end=" ")
#    for j in range(1, i + 1):
#        print("*", end=" ")
#    print()
# # # # Case 10
# n = int(input("Enter the number of rows: "))
# for i in range(1, n + 1):
#    print(" " * (n - i), end=" ")
#    for j in range(1, 2 * i):
#        print(j, end=" ")
#    print()
