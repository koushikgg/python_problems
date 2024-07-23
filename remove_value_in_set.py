def remove_value(set, value):
    if value in set:
        set.remove(value)
        return set
    else:
        return "item not found"

if __name__ == '__main__':
    new_set = {'a', 'b', 'c', 'd','e'}
    result = remove_value(new_set, 'd')
    print("after removing ",result)