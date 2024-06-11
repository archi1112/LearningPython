"""
List and tuples include duplicates but set and dictionary not

"""

# Lists
"""
List can contain any datatype
difference in insert and append : insert adds element in between but append adds element at end
Lists are mutable
"""
li=[23,4,5,6,7,"python","list"]
new_li=["fruit","vegetable","doctor"]
print(li)
# prints all starting from index 2
print(li[2:])
# negative indexing starts from last
print(li[-1])
concat_li=[li,new_li]
print(concat_li)
# lists are mutable we can change values
li[4]="555"
print(li)



# Tuples
"""
Tuples can also contain values of any datatype
 tuples are immutable we cannot modify values by index
"""
tup=(2,3,4,"the")
print(tup)


# tuples are immutable we cannot modify values by index
# tup[1]=44
# print(tup)

# concatenating two tuples
tup_second=("jack","spade")
print(tup_second)

tup_new=(tup,tup_second)
print(tup_new)

# sets
"""
use the concept of hash to store the elements
sets are immutable , cannot modify element using the index(indexing not supported becos of concept of hash) but can add elements at the end
"""
s={2,9,3,1,0}
print(s)
s={23,45,6,7,8,23,48}
print(s)
# s[2]="hey"
# print(S)



