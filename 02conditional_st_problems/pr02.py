# Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. 
# Everyone gets a $2 discount on Wednesday


# we take input from the user
age=int(input("Enter your age: "))

day=input("enter the day of week:").strip()
day=day.lower()

price = 12 if age >= 18 else 8

if day == "wednesday":
    price -= 2

print("ticket price for You is $",price)