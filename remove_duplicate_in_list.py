def remove_duplicates(list):
    unique_list = []
    for i in list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

sample_list = [1,2,4,1,3,4,2]
print(remove_duplicates(sample_list))