# methods of strigs

my_string = "  Hello, World!  "

# 1. strip() - removes leading and trailing whitespace
stripped_string = my_string.strip()


print(f"Stripped String: '{stripped_string}'")

# 2. lower() - converts string to lowercase
lowercase_string = my_string.lower()

# replace() - replaces a substring with another substring

replaced_string = my_string.replace("World", "Python") # strip() takes two arguments old substring and new substring


# we have strings with commas separated values
csv_string = "apple,banana,cherry,dates"


# now i want to convert this string into list of fruits
fruits_list = csv_string.split(",")  # split() method splits the string at each comma and returns a list

print(fruits_list)


# get position of substring in a string
position = my_string.find("World")  # it will return starting index of substring "World

# find will return -1 if substring is not found


# count the number of occurrences of a substring in a string


count_hello = my_string.count("l")  # it will count how many times 'l' is present in the string

# formating strings using f-strings
name = "Alice"
age = 30
print(f"hi my name is {name} and my age is {age}")

# curyl baraces know to be place holder  for variables inside f-strings

# another way of formating strings is using format() method
formatted_string = "hi mera  name is {} and my age is {}".format(name, age)
print(formatted_string)





# consider a lsit of strings
string_list = ["  apple  ", "  banana  ", "  cherry  "]
# i want to strip whitespace from each string in the list
stripped_list = [s.strip() for s in string_list]  # list comprehension to


# now print the stripped list
print(stripped_list) # ['apple', 'banana', 'cherry']

# convert this list into string 

# list_to_string ="".join(stripped_list)

# print(list_to_string)  # applebananacherry

# above we can have join with any separator

list_to_string =" ".join(stripped_list)
print(list_to_string)

# get length of string
length = len(my_string)
print(f"Length of the string: {length}")







