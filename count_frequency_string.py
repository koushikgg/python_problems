def char_occurence(str):
    new_dict={}
    for i in str:
        if i in new_dict:
            new_dict[i]+=1
        else:
            new_dict[i]=1
    return new_dict

if __name__ == '__main__':
    new_string="google.com"
    print(char_occurence(new_string))