def remove_key(dict, key):
    if key in dict:
        del dict[key]
        return dict
    else:
        return f"Key {key} is not found"
    
if __name__ == '__main__':
    new_dict = {
        "king": 3,
        "lion": 2,
        "dog": 4,
        "elephant": 1,
    }
    print(remove_key(new_dict, "lion"))