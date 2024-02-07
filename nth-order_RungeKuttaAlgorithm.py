#
#   nth-order_RungeKuttaAlgorithm.py
#
#   This example is of a second-order linear differential equation of non-constant coefficients. 
#   The program prompts the user for the coefficients of the function. The interval of integration
#   is predetermined and the differential equation exists along the set of real numbers — in this 
#   case, R². The numerical method implemented may be generalized to a higher-order differential 
#   equation, for an arbitrary n-value.
#
#___________________________________________________________________________________________________


# requests import of various libraries

import cmath;
import numpy as np;
import matplotlib.pyplot as plt;


# defines variables & functions of initial value problem

syms a, b, c, n, x;

syms y, y' = dy/dx, ϕ = ϕ(x);

f = a*y" + b*y' + c*y + d = 0; 

a = a(x); 

b = b(x); 

c = c(x);

d = d(x);

y(0) = y_0;



# defines the interval & prints a brief description of the problem to the user 

interval_x = fixed.Interval(0, 2);

problem = "The differential equation is defined by the general equation, 0 = a*y^2 + b*y + c, with an unknown initial condition, y(0).";

problem_details1 = "The solution will be the function, Ï†(x), of the general form, (insert generalized solution after running program).";

problem_details2 = "The differential equation of the problem exists along the interval, 0 ≤ x ≤ 2.";

disp(problem);

disp(problem_details);



# prints the general form of the differential equation 

general = "a*y" + b*y' + c*y + d = 0";

disp("The general form of the linear, second-order differential equation is " + general + ".");



# prompts user for coefficients of the differential equation

a(x) = int(input("Please input the explicit non-constant coefficient of each term, starting with a(x)."));

b(x) = int(input("Now, please input the coefficient, b(x)."));

c(x) = int(input("State the equation for the non-constant coefficient, d(x)."));

d(x) = int(input("Finally, write the function, d(x)."));



# determines the order of differential equation & assigns a variable to the value

n; 



# requests the initial condition & error tolerance (check term in text; ensure that latter exists for n < 4)

y_0 = int(input("Please enter the y-value of the initial condition at y(0)."));

ε = int(input("Enter the value of the tolerance."));  



# assigns a set of two coordinates 

(x, y); 



# defines the series of equations, k_n, for the value of n corresponding to the differential equation

S = 1:(i - 1);

for(int i: (length(x) - 1));
{
	k_i = f(t_n + 𝛼_i*h, x_n + h*(sum(S)) + (β_{i*j})*k_j;
}

k = array.k_i; # forms array of n terms in length from coefficients defined above

c = int(input("Enter the value of c.");



# assigns N-value 

N = int(input("Please enter the value of N.");



# sets step value of differential equation

h = (c - x_0)/N;



# calculates the solution for differential equations by Runge-Kutta method for n = 1

if(n = 1)
{
   x_1 = x_0 + h;

   y_1 = y_0 + (k_1)*h;

  disp("The final solution is the set of     equations, " + x_1 " and " + y_1 + ".");
}



# computes the solution to the differential equation by Runge-Kutta method, for n = 2

if(n = 2)
{
   x_2 = x_1 + h;

   y_2 = y_1 + h*(k_1 + k_2)/2;

   disp("The final solution is the set of equations, " + x_2 " and " + y_2 + ".";
}



# calculates a differential equation of third-order, where n = 3, by the Runge-Kutta method

if(n = 3)
{
	x_3 = x_2 + h;

    y_3 = y_2 + h*(k_1 + k_2 + k_3)/3;

    disp("The final solution is the set of equations, " + x_3 " and " + y_3 + ".");
}



# computes a fourth-order differential equation by the classical Runge-Kutta method

if(n = 4)
{
	x_4 = x_3 + h;

    y_4 = y_3 + (1/6)*(k_1 + 2*k_2 + 2*k_3 + k_4);

    disp("The final solution is the set of equations, " + x_4 " and " + y_4 + ".");
}



# solves differential equations by Runge-Kutta method for values of n = 5, the coefficients of which arise from the Cash-Karp parameters corresponding to the index, i

if(n = 5)
{
	x_5 = x_4 + h;

    c_1 = 37/378;

    c_2 = 0;

    c_3 = 250/621;

    c_4 = 125/594;

    c_5 = 0;

    c_6 = 512/1771;

    y_5 = y_4 + (c_1)*(k_1) + (c_2)*(k_2) + (c_3)*(k_3) + (c_4)*(k_4) + (c_5)*(k_5) + (c_6)*(k_6);

    disp("The final solution is the set of equations, " + x_5 " and " + y_5 + ".");
}



# finds the solution to the differential equation for orders, n > 5 
 
y_n = y_{n - 1} + c_{n}*h*(k_n)/n + O(h^{n + 1});

disp("The final solution is the set of equations, " + x_n " and " + y_n + ".");