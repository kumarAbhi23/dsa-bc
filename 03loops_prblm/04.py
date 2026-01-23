'''
reverse string using loop
s = "Hello, World!"

'''


s = "Hello, World!"

revesed_str=""
for char in s:
    revesed_str=char+revesed_str
    # EVERY iteration, add current char to the front of revesed_str 
    # print(revesed_str)


print("Reversed string:", revesed_str)     