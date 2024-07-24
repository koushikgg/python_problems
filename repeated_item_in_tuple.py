def find_repeated_items(tup):
    new_list = []
    for i in tup:
        if tup.count(i)>1 and i not in new_list:
            new_list.append(i)
    return new_list

if __name__=="__main__":
    new_tuple = ('Apple', 'Ball', 'Apple', 'Cat', 'Ball', 'Dog')
    print(find_repeated_items(new_tuple))

