import functools

def square(x):
    return x*x


def add(x,y):
    return x+y

def even(x):
    return x%2==0

def squarecube(x):                  # nested functions
    def square(y):
        return y*y
    return square(x*x*x)


print( add( square(5), square(6) ) )

nums = [1,2,3,4,5]

numsquares = list( map(square, nums) )          # apply square function on each item of nums array

print(nums)
print(numsquares)


# anonymous functions

square = lambda x: x*x

print( square(5) )

numsquares = list( map(lambda x: x*x, nums) )   # same as above but with anonymous functions

print( numsquares )


# filtering data

numbers = list( range(1,11) )       # create a list of 1 to 10

evens = list( filter(even, numbers))        #call even() on each item in numbers, returns only even numbers

print( numbers )

print( evens )


# applying a function that calculates a single result on a list

sum = functools.reduce(add, numbers)

print(sum)

x = squarecube(5)
print(x)