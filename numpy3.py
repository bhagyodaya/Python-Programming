import numpy as np
in1,in2=map(int,input("enter:").split())
out=np.eye(in1,in2,dtype=int)
print(out)