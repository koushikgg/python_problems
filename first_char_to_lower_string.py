def first_char_to_lower(str):
    return str[0].lower()+str[1:]
if __name__=="__main__":
    new_str = "Apple"
    print(first_char_to_lower(new_str))