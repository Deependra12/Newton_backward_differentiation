#Importing NumPy Library
import numpy as np
import sys

# Reading number of unknowns
n = int(input('Enter number of data points: '))

# Making numpy array of n & n x n size and initializing 
# to zero for storing x and y value along with differences of y
x = np.zeros((n))
y = np.zeros((n,n))
index = 0
flag = 0
sum = 0
    


# Reading data points
print('Enter data for x and y: ')
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']='))
    y[i][0] = float(input( 'y['+str(i)+']='))
    
# Generating backward difference table
for i in range(1,n):
    for j in range(n-1,i-2,-1):
        y[j][i] = y[j][i-1] - y[j-1][i-1]

##validating point of differentiation
while(flag ==0):

    num = float(input("Enter where you want to find the differentiation:"))
    for i in range(0,n):   
        if ((abs(num-x[i])) <0.0001):
            print(i)
            index = i
            print(index)
            flag = 1
                
        
        
    if(flag ==0):
        print("Invalid Calculation point. This point should be nearer to the x_points and can differ only by 0.0001")



print('\nBACKWARD DIFFERENCE TABLE\n')

for i in range(0,n):
    print('%0.2f' %(x[i]), end='')
    for j in range(0, i+1):
        print('\t%0.2f' %(y[i][j]), end='')
    print()
h = x[1] - x[0]
print(h)
    

print(index)
x=1
for i in range(1,index+1):
    print(y[index] [i])
    term =(y[index][i])/x
    x=x+1
    sum = sum + term
         

first_derivative = round((sum/h),3)

print("Reqd value is",first_derivative)

        
