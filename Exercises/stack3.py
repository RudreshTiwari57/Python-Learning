# from DSA.stack import Stack

# Given an array nums, for each element find the next greater element to its right.
# If there’s no greater element, return -1 for that position.
#         Input: [2, 1, 2, 4, 3]
#         Output: [4, 2, 4, -1, -1]


def find_greater(my_list,current_item: int
                 ,next_item : int,
                 flag = False
                 )      -> bool:
    if flag:
        print(my_list)
        return my_list[current_item]
    if next_item >= len(my_list)-1 and current_item >= len(my_list):
        return -1
    print(next_item)
    if my_list[current_item]>my_list[next_item]:
        find_greater(my_list,current_item, next_item, True)
    return find_greater(my_list,current_item, next_item+1)





# stack : Stack = Stack()
my_list : list[int] = [2, 1, 2, 4, 3]
ith = my_list[0]
for i in range(len(my_list)):
    print(find_greater(my_list,i,i+1))


