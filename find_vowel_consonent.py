VOWELS = "aeiouAEIOU"
def find_vowel_consonant(char):
    """
    finds vowel or consonent
    """
    if char.isdigit():
        return "Please enter an alphabet..!"
    if char in VOWELS:
        return f"{char} is a Vowel"
    else:
        return f"{char} is a Consonant"
    
if __name__ == '__main__':
    alphabet = input("Enter an alphabet: ")
    print(find_vowel_consonant(alphabet))