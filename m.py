import numpy as np
z=np.array(input("enter the 3 by 3 matrix z:"))
k=np.array(input("enter the 3 by 3 matrix k:"))
print "the det of a matrix z:",np.linalg.det(z)
print "the det of a matrix k:",np.linalg.det(k)
print "the inv of a matrix z:",np.linalg.inv(z)
print "the inv of a matrix k:",np.linalg.inv(k)
print "the eigen values of a matrix z:",np.linalg.eig(z)
print "the eigen values of a matrix k:",np.linalg.eig(k)
print "the rank of a matrix z:",np.linalg.matrix_rank(z)
print "the rank of a matrix k:",np.linalg.matrix_rank(k)
print "the transpose of a matrix z:",np.transpose(z)
print "the transpose of a matrix k:",np.transpose(k)
print "the addition of two matrices:",np.add(z,k)
print "the subtraction of two matrices :",np.subtract(z,k)
print "the multiplication of two matrices:",np.multiply(z,k)
print "the division of two matrices:",np.divide(z,k)
print "trace of matrix z:",np.trace(z)
print "trace of matrix k:",np.trace(k)
print "square of matrix z:",np.square(z)
print "square of matrix k:",np.square(k)



