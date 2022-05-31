# handle edge cases
a = "['apple', 'banana', 'cola']"
b = ['apple']
c = []

"""
INPUT -> any of the above kind of lists
OUTPUT -> "apple, banana, cola"
"""

def stringConvertor(x):
    return [y.strip() for y in eval(x)]

def listConvertor(x):
    return list(x)

def checker(x):
    if(isinstance(x , str)):
        return stringConvertor(x)
    elif(isinstance(x , list)):
        return listConvertor(x)
    else:
        return 0

def convertor(x):
    return ", ".join(element for element in checker(x))


# test
# print(convertor(a))
# print(convertor(b))
# print(convertor(c))

