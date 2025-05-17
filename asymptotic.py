#Time complexity => this is the no. of steps required to complete an algorithm depending on the size of the input(n)
#constant Time complexity 0(1) => Time remains constant

def printNumber(n):
    steps = 0
    print(f"the number is, {n}")
    steps += 1
    print(f"The number of steps is {steps}")


printNumber(10)    
printNumber(100)    
printNumber(1000)    

#linear time complexity Big O(n) => steps increase linearly with the input e.g a loop
def OnTime(n):
    steps = 0
    for i in range(1, n + 1):
        steps += 1
    print(f"when n is {n}, the steps are {steps}")


OnTime(5)  
OnTime(10)  
OnTime(15)       

#quadratic time complexity Big O(n^2) => the steps increase quadratically e.g nested loops

def ONsquared(n):
    steps = 0
    for i in range(0, n):
        for j in range(0,n):
            steps += 1
    print(f"When n is {n}, the steps are {steps}")

ONsquared(8)
ONsquared(2)
ONsquared(5)

