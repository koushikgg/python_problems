def find_common(list1):
    """this will append elements to second list"""
    second_list = []
    for i1 in list1:
        second_list.append(i1)
    return second_list

if __name__ == '__main__':
    list1 = [14, 72, 36, 4, 5]
    print(find_common(list1))
