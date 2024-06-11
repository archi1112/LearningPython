# lambda expressions/functions

func=lambda num : num * num

print(func(4))

def is_even(numsarray):
        return numsarray%2==0


numsarray=[2,3,4,5,6]

# filter functions
# res=list(filter(is_even,numsarray))
res=list(filter(lambda n : n%2==0 , numsarray))
print(res)


# map functions
double=list(map(lambda d : d+2 , res))
print(double)


# special variable name
print(__name__)