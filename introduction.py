#Time complexity => time/steps taken to complete an algorithm
#Space complexity => space used to complete an algorithm

def func1(number):
    return number*(number + 1) /2
#func1 has constant time 0(1) complexity => because it doesn't matter the number you give - it does the operation in 1 operation


def func2(number):
    sum = 0
    for i in range(1, number+1): #steps depend on the number given 
        sum += i
    return sum

#func2 has linear time complexity 0(n) => the steps taken to complete the operation depends on the input(n) given examples loops 

print(func1(5))
print(func2(5))    

print(func1(10))
print(func2(10))    