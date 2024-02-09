"""8. Write a version of a palindrome recognizer that also accepts phrase
palindromes such as "Go hang a salami I'm a lasagna hog.",
"Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis",
"Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas",
"I roamed under it as a tired nude Maori", "Rise to vote sir",
or the exclamation "Dammit, I'm mad!".
Note that punctuation, capitalization, and spacing are usually ignored."""

def palindrome(word):
    before=""
    after=""
    for b in word:
        if(b.isalpha()):
            before+=b.lower()
    for a in range(len(before)-1,-1,-1):
        after+=before[a]
    if(before==after):
        return "Is palindrome"
    else:
        return "Not palindrome"

def main():
    while(5==5):
        word=input("Please enter word or sentence to recognizer palindrome:")
        print(palindrome(word))
main()        
        
