from collections import defaultdict

def split_by_first_character(words_list):
    '''this method will split by first character'''
    split_dict = defaultdict(list)
    
    for word in words_list:
        first_char = word[0]
        split_dict[first_char].append(word)
    
    return dict(split_dict)


if __name__ == '__main__':
    words_list = ['virat', 'kohli', 'maxi', 'abd', 'gayle']
    split_dict = split_by_first_character(words_list)

    for key, value in split_dict.items():
        print(f"{key}: {value}")