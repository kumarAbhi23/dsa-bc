'''
yiled statement in python
A function which contains yield statement is called generator function


write a grenerator function that yiled even number up to specified limit


'''

# lets see first normal function which returns list of even numbers up to limit
def even_numbers_list(limit):
      for num in range(2,limit+1,2):
          return num

# result = even_numbers_list(10)
# print("Even numbers up to 10 are:", result)

# but it will return only first even number because of return statement and if i use list to store all even numbers and 
# return it then it will consume more memory if limit is large


# better solution is to use generator function with yield statement 

#yiled statement is used to return a value from gnerator function and pause its execution state so that it can be resumed later

def even_number_generator(limit):
    for num in range(2, limit+1, 2):
        yield num  # yield even number and pause execution  

# using the generator function
even_gen = even_number_generator(10)
print(even_gen) # it will print generator object and objeect is iterable

for even_num in even_gen:
    print("Even number:", even_num)  # it will print even numbers one by one
