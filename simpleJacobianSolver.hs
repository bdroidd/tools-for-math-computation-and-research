#
#  simpleJacobianSolver.hs
#
#  
#
#
#
#
#____________________________________

# defines symbols utilized in the algorithm

x y z

f = xy^2 + 10z


# defines three distinct equations for a new system of linear equations 

(del_F)/(del_x) = y^2 # verify notation

(del_F)/(del_y) = 2xy

(del_F)/(del_z) = 10


# instantiates an array that describes the Jacobian row vectoe & adds equations of SLE to the array

J = [(del_F)/(del_x), (del_F)/(del_y), (del_F)/(del_z)]


# prints the Jacobian to the user