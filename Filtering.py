from functools import reduce
def is_even(n):

    return n %2 == 0

nums=[1,4,3,2,5,7,6]

print('Use the lambda exprition or Function for one use instead def function:')
print('list(filter(is_even,nums)')
evens = sorted(list(filter(is_even,nums)))
print('Use Function:')
print(evens)
print('list(filter(lambda n : n%2==0 ,nums)) :')
print('Use Lambda:')
evens = sorted(list(filter(lambda n : n%2==0 ,nums)))
print(evens)
double=list(map(lambda n:n*2,evens))
print(double)
sum=reduce(lambda  a,b:a+b ,double)
print(sum)
