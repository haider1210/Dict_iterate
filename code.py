# we can use items in built function in the dictionary with keys and  values
# Dictionary in Python is an unordered collection of data values that are used to store data values like a map. Unlike other Data Types that hold only single value as an element, the Dictionary holds key-value pair. In Dictionary, the key must be unique and immutable. This means that a Python Tuple can be a key whereas a Python List can not. A Dictionary canbe created by placing a sequence of elements within curly {} braces, separated by ‘comma’.

#Defaultdict is a container like dictionaries present in the module collections. Defaultdict is a sub-class of the dictionary class that returns a dictionary-like object. The functionality of 
#both dictionaries and defaultdict are almost same except for the fact that defaultdict never raises a KeyError. It provides a default value for the key that does not exists.


d=dict()
for num in nums:
  if num in nums:
    d[num] =+ 1
  else:
    d[num]=1
for key ,values in d.items():
            if values >n//2:
                return key

  ---Default dictionary :
# Python program to demonstrate 
# defaultdict 


from collections import defaultdict 


# Function to return a default 
# values for keys that is not 
# present 
def def_value(): 
	return "Not Present"
	
# Defining the dict 
d = defaultdict(def_value) 
d["a"] = 1
d["b"] = 2

print(d["a"]) # 1
print(d["b"]) # 2
print(d["c"]) # Not Present
