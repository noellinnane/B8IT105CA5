from functools import reduce

#Addition with a list
#Using Reduce function

def sum1(values):
    return reduce(lambda x,y: x+y, values)

print(sum([1,2,3,4]))


#Addition with 2 lists
#Using Map function

def sum2(list1, list2):
    return list(map(lambda x,y: x+y, list2, list2))

print(sum2([1,1],[1,1]))

#Subtraction with a list
#Using Reduce function

def sub1(values):
    return reduce(lambda x,y: x-y, values)

print(sub1([2,1]))

#Subtraction with 2 lists
#Using map function

def sub2(list1, list2):
    return list(map(lambda x,y: x-y, list1, list2))

print(sub2([2,2],[1,1]))

#Muliplication with list
#Using Reduce Function

def mult1(values):
    return reduce(lambda x,y: x*y, values)

print(mult1([5,5]))

#Multiplication with 2 lists
#Using Map function

def mult2(list1, list2):
    return list(map(lambda x,y: x*y, list1, list2))

print(mult2([5,5],[5,5]))

#Division with list
#Using Reduce function

def div1(values):
    return reduce(lambda x,y: x/y, values)
    
print(div1([2,1]))

#Division with 2 lists
def div2(list1, list2):
    return list(map(lambda x,y: x/y, list1, list2))

print(div2([2,3],[1,2]))


#Square List

def sq1(values):
    return list(map(lambda x: x**2, values))

print(sq1([1,2,3,4,5]))

#Square Generator v1
# Generate list of squares for whole list
def sqr2(y):
    return list(x**2 for x in range(y))
    
print(list(sqr2(9)))


#Square Generator v2
# Iterate between squares
def sqr3(values):
    return (x**2 for x in range(values))

a = sqr3(9)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
