#
#  IVP_PicardMethod.py
#
#  The technique implemented in this program is Picard's method, which can 
#  be used to resolve initial value problems of the first order. In this 
#  particular case, a value is given for y(x_0), along with a domain, for a preset
#  differential equation. The program prints the solution to the user.
#_____________________________________________________________________________


import numpy as py

# introduces the variables & defines initial values 

syms x;

y(0) = 0;

y_0 = 0;

x > -1; % fix formatting 


# defines the initial differential equation 

y'(xy + y - 2x - 2) = ln(x + 1);

y' = ln(x + 1)/(xy + y - 2x - 2);


# calculates the integral of the rearranged differential equation 

y = int(y');


# defines the general equation using Picard's theorem 

phi_{n + 1} = f(t, phi_n (t)), x_n, x);


# computes the terms of the particular solution*

phi0 = 0;

phi1 = int(f(t, phi_0 (t)), x_1, x);

phi2 = int(f(t, phi_1 (t)), x_2, x);

phi3 = int(f(t, phi_2 (t)), x_3, x);

phi4 = int(f(t, phi_3 (t)), x_4, x);

solution = phi0 + phi1 + phi2 + phi3 + phi4;


# displays the final solution to the user

print('The solution to the initial value problem is ' + solution + '.');