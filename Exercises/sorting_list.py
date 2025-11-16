def sort_my_list(my_list : list[int],
                 index : int,
                 next : int
                 )      -> list[int]:
    if index>=len(my_list)-1:
        return my_list
    if next >= len(my_list):
        return sort_my_list(my_list, index+1,index+2)
    if my_list[next] > my_list[index]:
        my_list[next],my_list[index] = my_list[index],my_list[next]
    return sort_my_list(my_list,index,next+1)



my_list: list[int] = [54745,23,4,456,456,68,678,6789,789,78,90,8,0,99,9,00,97,867,856,74,64,6,3454,6,45,667]
print(sort_my_list(my_list,0,1))