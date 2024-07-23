def delete_first_occurence(arry, element):
    """ this method will remove the first occurence of element
    """
    new_array=arry
    for i in range(len(arry)):
        if new_array[i] == element:
            new_array.remove(new_array[i])
            return new_array

if __name__ == '__main__':
    array = [1,2,3,4,3,5]
    element = 3
    new_array = delete_first_occurence(array, element)
    print(f"this is the output array", new_array)