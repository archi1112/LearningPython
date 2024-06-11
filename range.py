from itertools import chain

"""
range function
float not allowed
using chain method-concatenate 2 ranges : chain()
accesing any particular index in range series : range(2)[0]
In range the start , stop , step should always be integer
"""

start=2
stop=10
step=2
# stop is not included it is exluded from the series
for i in range(start,stop,step):
    print(i)


# float number not allowed in range
# for i in range(2.3):
#     print(i)

# using chain method 
# result of two range can be concatenated

res=chain(range(5), range(10,20,2))
for i in res :
    print(i)
print()


# accessing range with index value
# in the series of 5 prints the second index value
ele=range(5)[2]
print(ele)


