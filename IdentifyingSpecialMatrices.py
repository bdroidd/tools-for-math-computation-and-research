# 
# IdentifyingSpecialMatrices.py
#
# The program traps different types of special matrices 
# (non-invertible, idempotent, or otherwise) before 
# calling on the set of functions that carry out the 
# inversion routine on a 4x4 matrix. Afterwards, the 
# type of special case encountered is classified. This 
# piece of code then determines whether the matrix is 
# singular or not.
#______________________________________________________

import numpy as np

# makes B a copy of the matrix, A, before the values are altered
def isSingular(A) :
    B = np.array(A, dtype=np.float_) 
    try:
        fixRowZero(B)
        fixRowOne(B)
        fixRowTwo(B)
        fixRowThree(B)
    except MatrixIsSingular:
        return True
    return False
    
 # defines the error flag
 class MatrixIsSingular(Exception): pass
 
 # defines the first row, Row Zero
 def fixRowZero(A) :
    if A[0,0] == 0 :
        A[0] = A[0] + A[1]
    if A[0,0] == 0 :
        A[0] = A[0] + A[2]
    if A[0,0] == 0 :
        A[0] = A[0] + A[3]
    if A[0,0] == 0 :
        raise MatrixIsSingular()
    A[0] = A[0] / A[0,0]
    return A
    
 # sets sub-diagonal elements to zero, then defines Row One
 def fixRowOne(A) :
    A[1] = A[1] - A[1,0] * A[0]
    if A[1,1] == 0 :
        A[1] = A[1] + A[2]
        A[1] = A[1] - A[1,0] * A[0]
    if A[1,1] == 0 :
        A[1] = A[1] + A[3]
        A[1] = A[1] - A[1,0] * A[0]
    if A[1,1] == 0 :
        raise MatrixIsSingular()
    A[1] = A[1] / A[1,1]
    return A
    
 # defines Row Two
 def fixRowTwo(A) :
    A[2] = A[2] - A[2,0] * A[0]
    if A[2,1] == 0 :
        A[2] = A[2] + A[2]
        A[2] = A[2] - A[2,0] * A[0]
    if A[2,1] == 0 :
        A[2] = A[2] + A[3]
        A[2] = A[2] - A[2,0] * A[0]
    if A[2,2] == 0 :
        raise MatrixIsSingular()
    A[2] = A[2] / A[2, 2]
    return A
    
    # tests whether diagonal element is zero or not
    if A[2,2] == 0 :
        A[3] = A[2, 0] + A[3, 0]
        A[3] = A[2, 1] + A[3, 1]
        A[3] = A[3] - A[3,0] * A[0]
    if A[3,1] == 0 :
        A[3] = A[3] + A[3]
        A[3] = A[3] - A[3,0] * A[0]
    if A[3,3] == 0 :
        raise MatrixIsSingular()
    A[3] = A[3] / A[3, 3]
    return A
    
    if A[2,2] == 0 :
        raise MatrixIsSingular()
        A[3] = A[3] / A[3, 3]
    return A
    
    # defines row three
    def fixRowThree(A) :
    A[3] = A[3] - A[3,0] * A[0]
    if A[3, 0] != 0 :
        A[3, 0] = [3,0] * A[0]
    if A[3, 1] != 0:
        A[3, 1] = [3, 1] * A[0]
    if A[3, 2] != 0:
        A[3, 2] = [3, 2] * A[0]
        
    # tests if the diagonal element is zero
    if A[3,3] == 0 :
        raise MatrixIsSingular()
        A[3] = A[3] / A[3, 3]
    return A
    
    # sets the diagonal element of Row Three to one
    def fixRowThree(A) :
    A[3] = A[3] - A[3,0] * A[0]
    if A[3,1] == 0 :
        A[3] = A[3] - A[3,0] * A[0]
    if A[3,2] == 0 :
        A[3] = A[3] - A[3,0] * A[0]
    if A[3,3] == 0 :
        A[3, 3] = A[0, 0] + A[3, 3]
        raise MatrixIsSingular()
    A[3] = A[3] / A[3,3]
    return A
    
    
