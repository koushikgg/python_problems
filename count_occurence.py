def count_occurence(arry, element):
    """ this method will count the occurence of element
    """
    count=0
    for i in range(len(arry)-1, -1, -1):
        if array[i] == element:
            count+=1
    return count

if __name__ == '__main__':
    array = [1,2,3,4,3,5]
    element = 3
    occurence_of_element = count_occurence(array, element)
    print(f"this is the occurence of {element} is ", occurence_of_element)