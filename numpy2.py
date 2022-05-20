#it is necssary to give the 9 elements 
import numpy as np
input1=list(map(int,input("Enter:").split()))
out=np.array(input1)
out.shape=3,3
print(out)