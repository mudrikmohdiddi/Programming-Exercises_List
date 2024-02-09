"""2. Lottery Number Generator
Design a program that generates a seven-digit lottery number. The program should generate
seven random numbers, each in the range of 0 through 9, and assign each number to a
list element. (Random numbers were discussed in Chapter 6.) Then write another loop that
displays the contents of the list."""

list_number=[]
number=""
for i in range(7):
    number=""
    random_number=[0,1,2,3,4,5,6,7,8,9]
    del random_number[(7-i):(10-i)]

    for i in range(7):
        number+=str(random_number[i])
    list_number.append(number)
for i in list_number:
    print(i)


        
