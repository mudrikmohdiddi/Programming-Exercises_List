"""1. Total Sales
Design a program that asks the user to enter a store’s sales for each day of the week.
The amounts should be stored in a list. Use a loop to calculate the total sales for the week and
display the result."""

day=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
stored_sales=[]
total_sales=0
for i in range(len(day)):
    sales=float(input(f"Please enter a store’s sales for {day[i]}:"))
    while(sales<0):
        print("\nYou enter wrong input please try angain:")
        sales=float(input(f"Please enter a store’s sales for {day[i]}:"))
    stored_sales.append(sales)
for i in stored_sales:
    total_sales+=i
print(f"The total sales for the week is {total_sales} TZS")

