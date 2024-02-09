"""5. A pangram is a sentence that contains all the letters of the English alphabet at least once,
for example: The quick brown fox jumps over the lazy dog.
Your task here is to write a function to check a sentence to see if it is a pangram or not."""

def pangram(sentance):
    list=[]
    for i in sentance:
        if(i.isalpha()):
            list.append(i.lower())
    sum=0
    for i in set(list):
        sum+=1
    if(sum==26):
        return "Pangram"
    else:
        return "Not pangram"
def main():
    while(1==1):
        sentance=input("Please enter sentance:")
        print(f"The sentance is {pangram(sentance)}")
main()        
