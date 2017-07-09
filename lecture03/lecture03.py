# find the square root of a perfect square 

# x = 16 
# ans = 0   #counter variable 
# while ans*ans <= x:
#     ans = ans + 1
# print(ans)


# Is the number Even or Odd?
# 
# if (x/2)*2 == x:
#     print("Even")
# else:
#     print("Odd")


# x = 150 #the number we are testing in this case
# ans = 0 #counter variable 

# if x >= 0:
#     while ans*ans < x:
#         ans = ans +1
#         print("ans=", ans)
#     if ans*ans != x:
#         print(x, 'is not a perfect square')
#     else: print(ans)
# else: print( x, ' is a negative number')

 
# #what are all the divisors of an integer?
x = 10
i = 1 #counter is initalized 
while i < x: #the end test
    if x%i === 0:
        print('divisor', i)
    i = i +1

# #the for loop does the same thing as the divisor above
# x = 10 
# for i in range(1,x): #give you all numbers up to, but not including x
#     if x%i == 0:
#         print('divisor:', i)


x = 1515361
if x > 0:
    for ans in range(1,x):
        if ans*ans == x:
            print(ans)
            break



#collect the divisors that are printed as we go along
x = 100
divisors = ()
for i in range(1,x):
    if x%i == 0:
        divisors = divisors + (i)


#run a loop where I need to collect things together 
#




























