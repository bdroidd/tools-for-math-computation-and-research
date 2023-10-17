#
#   LaplaceTransformSolver_PiecewiseCase.py
#
#   The following program applies the LaPlace transform method to a set of 
#   three specific piecewise functions to determine its solution.
#______________________________________________________________________________

import matplotlib.pyplot as plt
import numpy as np

syms t

f = piecewise(0 < t < 1, 1, 1 < t < 2, -2, 2 < t, t^2);

F = laplace(f);

disp(F)