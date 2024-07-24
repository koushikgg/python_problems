def reverse_string(str):
    new_str=''
    for i in str:
        new_str=i+new_str
    return new_str

if __name__ == '__main__':
    new_string="google.com"
    print(reverse_string(new_string))