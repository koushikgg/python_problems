def iterate_dictionary(d):
    for key, value in d.items():
        print(f"Key is : {key}, Value is : {value}")

if __name__ == '__main__':        
    new_dict = {
        "king": 3,
        "lion": 2,
        "dog": 4,
        "elephant": 1,
    }

    iterate_dictionary(new_dict)