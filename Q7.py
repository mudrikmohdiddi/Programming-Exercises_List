"""7. Write a function filter_long_words() that takes a list of words and
an integer n and returns the list of words that are longer than n."""

def long_words(word,integer):
    list_long_word=[]
    list_word=word.split(",")
    for i in list_word:
        if(len(i)>integer):
            list_long_word.append(i)
    return f"List of words that are longer than {integer} length of string is {list_long_word}"
def true_integer(no):
    try:
        intege=int(no)
        return True
    except ValueError:
        return False
def main():
    while(1==1):
        word=input("Please enter list of word:")
        number=""
        while((" " in word) or ("," not in word)):
            if(" " in word):
                print("Please don't enter space in word, try again")
            elif("," not in word):
                print("Please enter commer, try again")
            word=input("Please enter list of word:")
        integer=input("Please enter integer:")
        while(true_integer(integer)==False):
            print("You enter wrong input, try again")
            integer=input("Please enter integer:")
        print(long_words(word,int(integer)))
main()
        
            
