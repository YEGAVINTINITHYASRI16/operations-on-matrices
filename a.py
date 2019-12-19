#appending program
import numpy as np
c=np.array(input("enter the elements of c:"))
n=np.array(input("enter the elements of n:"))
print("the first array is:",c)
print("the second array is:",n)
l=len(c)
for i in range(0,l):
	c=np.append(c,n[i])
print("the array formed by appending is:",c)
