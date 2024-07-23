def track_count(str):
    """ this will count the occurence of characters
    """
    char_count = {}
    for char in str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

if __name__ == '__main__':
    string = "w3resource"
    result = track_count(string)
    print("count of string: ", result)