"""3. Rainfall Statistics
Design a program that lets the user enter the total rainfall for each of 12 months into a list.
The program should calculate and display the total rainfall for the year, the average monthly
rainfall, and the months with the highest and lowest amounts."""

month=["January","February","March","April","May","June","July","August","September","October","November","December"]
rain_full=[]
total_rain=0
high_rain=0
high_month=month[0]
lower_month=month[0]
for i in range(len(month)):
    rain=float(input(f"Please enter the total rainfall for {month[i]}:"))
    rain_full.append(rain)
    total_rain+=rain
    if(high_rain<rain):
        high_rain=rain
        high_month=month[i]
lower_rain=high_rain
for i in range(len(month)):
    if(lower_rain>rain_full[i]):
        lower_rain=rain_full[i]
        lower_month=month[i]
print(f"\nThe total rainfall for the year is {total_rain}")
print(f"\nThe average monthly rainfall is {total_rain/len(month)}")
print(f"\nThe highest rain full is {high_rain} at {high_month}")
print(f"\nThe lowest rain full is {lower_rain} at {lower_month}")
    
    

