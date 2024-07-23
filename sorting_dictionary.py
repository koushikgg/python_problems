def sort_dictionary(dictionary):
    ascending_order = dict(sorted(dictionary.items(), key=lambda item: item[1]))
    decending_order = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse = True))

    return ascending_order, decending_order

if __name__ == '__main__':
  
    new_dict = {
        "apple": 3,
        "mango": 2,
        "orange": 4,
        "lemon": 1,
    }

    ascending_order, decending_order = sort_dictionary(new_dict)
    print("Ascending_order", ascending_order)
    print("Decending_order", decending_order)