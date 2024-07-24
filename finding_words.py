def find_words(list, n):
    new_list = []
    for items in list:
        if len(items) > n:
            new_list.append(items)
    return new_list

if __name__ == '__main__':
    my_list = ["apple", "ball", "baloon", "elephant", "lion"]
    print(find_words(my_list, 3))