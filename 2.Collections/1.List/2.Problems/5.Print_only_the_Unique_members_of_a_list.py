# # # Method 1
# input_list = [1, 2, 3, 4, 4, 3]
# # # my_list = []
# # # for i in input_list:
# # #    if i not in my_list:
# # #        my_list.append(i)
# # # print(my_list)


# # # Method 2
# my_list = [1, 2, 3, 4, 4, 3]
# my_set = set(my_list)
# print(list(my_set))


# # # Method 3 :Doubt .. How this code is working
# my_list = ["a", "b", "a", "c", "c"]
# my_list = list(dict.fromkeys(my_list))
# print(my_list)
