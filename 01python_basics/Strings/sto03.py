# handling path in python  

# txt_1 ="He said, "Hello, how are you? " "

# print(txt) # SyntaxError: invalid syntax

# as we can see above code gives syntax error because of nested double quotes  

# to fix this we can use escape character \ before the nested double quotes

txt ="He said, \"Hello, how are you? \" "

print(txt)  # He said, "Hello, how are you? "

# but using escape characters makes code less readable and also in windows file paths we have to use 
# \ which can create confusion

text_path = "C:\\new_folder\\test_file.txt"

# to avoid this we can use raw strings by prefixing string with r or R



raw_txt = r"C:\new_folder\test_file.txt"

# r before string tells python to treat backslashes as literal characters and not as escape characters
 

# containg in string 

text_new="Hello, welcome to python programming"

print("welcome" in text_new)  # True