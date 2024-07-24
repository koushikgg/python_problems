def find_common(list1, list2):
    """this will find the common elements in two list"""
    commom = []
    for i1 in list1:
        for i2 in list2:
            if i1 == i2:
                commom.append(i1)
    return commom

if __name__ == '__main__':
    list1 = [14, 72, 36, 4, 5]
    list2 = [5, 36, 72, 8, 9]
    print(find_common(list1, list2))
