# to print a reverse of space seperated sequence by user but return list should be in float format
import numpy as np
input1=list(map(float,input("Enter").split()))
arr=np.array(input1)
print(arr[::-1])