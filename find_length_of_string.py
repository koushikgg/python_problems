def get_length(str):
    count=0
    for i in str:
        count+=1
    return count



if __name__ == '__main__':
    new_string="abcde"
    print(get_length(new_string))