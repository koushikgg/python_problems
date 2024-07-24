def reverse_tuple(tup):
    new_list = []
    for i in tup:
        new_list.insert(0,i)
    new_tuple= tuple(new_list)
    return new_tuple

if __name__=="__main__":
    new_tuple = ('Apple', 'Ball', 'Cat', 'Dog')
    print(reverse_tuple(new_tuple))

