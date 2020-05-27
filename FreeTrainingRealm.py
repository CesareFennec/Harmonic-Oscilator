import numpy as np
import random
#bubble sort practice
def bubble_sort(alist):
    n = len (alist)
    for j in range(n-1):
        count = 0
        for i in range(0,n-1-j):
            if alist [i] > alist [i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
                count +=1
        if count == 0:
            break

X1=random.uniform(0,300)
X2=random.uniform(0,300)
X3=random.uniform(0,300)
alist = [X1,X2,X3]
print(alist)
bubble_sort(alist)
X=np.array(alist)
print(X)

#ANOTHER DIRECT WAY OF SORTING
def refined_bubble()