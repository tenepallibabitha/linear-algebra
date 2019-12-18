#generating 3*3 matrix
import numpy as np
import numpy.matlib
lp=np.matrix("1,2,3;4,5,6;7,8,9")
print lp
#inverse of a matrix
import numpy as np
from scipy import linalg
a=np.matrix("1,2,3;4,5,6;9,4,3")
b=linalg.inv(a)
print "inv=",b
#solving linear equations
import numpy as np
from scipy import linalg
c=np.array([[1,2],[2,5]])
print c
d=np.array([[5,6],[1,2]])
print d
e=np.linalg.solve(a,b)
print "ans=",e
#finding det of a matrix
f=np.matrix([[1,4],[5,6]])
print "matrix=",f
h=linalg.det(f)
print "det=",h
#finding eigen values
g=linalg.eig(c)
print "eigen values=",g
#matrix power
l=np.linalg.matrix_power(c,3)
print "matrix power=",l
#dot product of two arrays
j=np.dot(c,d)
print "dot product=",j
#matrix multiplication
k=np.matmul(c,d)
print "mul of two matrix=",k
#ones matrix
import numpy.matlib
import numpy as np
print np.matlib.ones((3,3))
#zeros matrix
import numpy.matlib
import numpy as np
print np.matlib.zeros((3,3))











