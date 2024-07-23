def reverse_array(arry):
    """ this method will reverse the array
    """
    reverse_arry = []
    for i in range(len(arry)-1, -1, -1):
        reverse_arry.append(arry[i])
    return reverse_arry

if __name__ == '__main__':
    array = [2, 4, 6, 8, 10]
    reverse_array = reverse_array(array)
    print("reversed array is ", reverse_array)