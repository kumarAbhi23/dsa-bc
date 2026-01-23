'''
Docstring for 05Functions.03prb

create a function which will return area and circumference of circle when radius is passed to it
'''


def area_circumference(radius):
    pi=3.14
    # we can also use math.pi by importing math module
    area=round((pi*radius*radius),2)
    circumference=round((2*pi*radius),2)
    return area,circumference
    
area, circumference = area_circumference(5) 
print("Area is:", area)
print("Circumference is:", circumference)          