"""6. Write a function find_longest_word()
that takes a list of words and returns the length of the longest one."""

def longest_word(word):
    word_list=word.split(",")
    large=0
    word_large=""
    for i in word_list:
        if(large<len(i)):
           large=len(i)
           word_large=i
    return f"The longest word is {word_large} at length of {large}"
def main():
    word=input("Please enter list of word:")
    for i in word:
        if(i.isdecimal()):
            number=i
    while((" " in word)==True or ("," in word)==False):
        if(" " in word):
            print("You enter space, please try angain")
        else:
            print("You don't enter commer, please try again")
        word=input("Please enter list of word:")
    print(longest_word(word))
main()

    

