//
//  constantCoefficients_ODESolver.java
//
//   This program computes the roots of the auxiliary equation of a
//   second-order homogeneous differential equation with constant 
//   coefficients, classifies the types of roots, and then displays the
//   resultant general solution for all possible cases. The sub-section
//   in which the roots of the indicial equation are computed utilizes the 
//   quadratic equation. There are two test drivers at the end of the 
//   program, the first of which generates random numbers for the coeffic-
//   ients and initial values of the DE and the latter of which prompts the 
//   user to enter these numbers.
//______________________________________________________________________________

import java.util.Random;
import java.util.Scanner;
import java.util.Math;
import java.io.*;

public class Main
{
    int real, imaginary;

    // instantiates a differential equation with arbitrary constant coefficeints & initial 
    // values (that will later be determined by a random number generator or a user)

    public static void double differentialEquation(int a, int b, int c, int y(0), int y(1))
    {
        double DifferentialEquation = a * y" + b * y' + c * y = 0;

        int y(0);

        int y(1);

        System.out.println("The second-order differential equation is " + differentialEquation + 
        " which has the initial values, y(0) and y(1).");
    }


    // prompts the user for the coefficients of the differential equation & its initial values

    public static void CoefficientDeterminer()
    {
        System.out.println("Input the coefficients of the differential equation and its initial values.");

        System.out.println("Write the value of a.");

        Scanner A = new Scanner(A.newline());

        double a = A

        System.out.println("Write the value of b.");

        Scanner B = new Scanner(B.newline());

        double b = B;

        System.out.println("Write the value of c.");

        Scanner C = new Scanner(C.newline());

        double c = C;

        System.out.println("Write the integer of y at x = 0.");

        Scanner x_0 = new Scanner(x_0.nextline());

        double y(0) = x_0;

        System.out.println("Write the integer of y at x = 1.");

        Scanner x_1 = new Scanner(x_0.nextline());

        double y(1) = x_1;

        
        // instantiates a standard auxiliary equation for the entire differential equation 

            Indicial r^2 + b*r + (c/a) = 0; // verify process for instantiating a function in Java


        // computes the specific indicial equations

            Indicial;


        // calculates the roots of the auxillary equations & defines two new variables for each resultant root 

            double q_a = a;

            double q_b = b;

            double q_c = c;

            double r1 = (- q_b - Math.sqrt(((q_b)^2 - 4 * (q_a) * (q_c)))/(2 * (q_a));

            double r2 = (- q_b + Math.sqrt(((q_b)^2 - 4 * (q_a) * (q_c))))/(2 * (q_a));

        if (r1 = r2)
        {
            double r = r1;

            System.out.println("The root is + " + r + ".");
        }

        else if (r1 != r2)
        {
            System.out.println("The resultant roots are " + r1 + " and " + r2 "."");
        }
            
        else
        {
            System.out.println("The roots are not real.");
        }
    }            


    // generates a complex number, for which the values of the real & imaginary components are set by the user

    public ComplexNumber(int r, int i)
    {
        this.real = r;

        this.imaginary = i;
    }


    // defines the conditions for the classification of the roots 

    public static void rootClassifier()
    {

        double C1, C2, r;
 
        if (r1 != r2)
        {
            double y(x) = C1 * e^{r1 * x} + C2 * e^{r2 * x};

            System.out.println("Since the roots are real and distinct, the final solution is y(x) = 
            C1 * e^{r1 * x} + C2 * e^{r2 * x}.");

            System.out.println("The exact solution to the differential equation is " + y(x) + ".");
        }

        else if (r1 = r2)
        {
            double r = r1;

            double y(x) = C1 * e^{r * x} + C2 * e^{r * x};

            System.out.println("Since the two roots are identical and belong to the set of reals, the final 
            solution will be of the general form, y(x) = C1 * e^{r * x} + C2 * e^{r * x}."); 

            System.out.println("The exact solution to the differential equation is " + y(x) + ".");
        }

        else if ((isNaN(r1) & isNan(r2) == TRUE) & (r1 != r2))
        {
            double α = - (q_b)/(2 * q_a);

            double β = sqrt(((4 * q_a * q_c) - (q_b)^2) / (2 * a));

            double y(x) = C1 * e^{α * x} * cos(β * x) + C2 * e^{α * x} * sin(β * x);

            System.out.println("Given that the roots are complex and distinct, y(x) = C1 * e^{αx} 
            * cos(βx) + C2 * e^{αx} * sin(βx).");

            System.out.println("The exact solution to the differential equation is " + y(x) + ".");
        }

            else
            {
                System.out.println("The differential equation does not have a solution.");
            }
    }

    // driver, which tests the methods above, solving the second-order differential equation with 
    // randomly generated coefficients & initial values

    public static void main(String[] args)
    {
        // defines a random number generator

            Random rand = new Random();

        // instantiates differential equations, with values of constant coefficients from random number generation 

            double a = a.rand();

            double b = b.rand();

            double c = c.rand();

            double x_0, x_1;

            x_0 = x_0.rand();

            x_1 = x_1.rand();

            y(0) = x_0;

            y(1) = x_1;

            differentialEquation ODE = new DifferentialEquation(a, b, c, y(0), y(1));

            System.out.println("The differential equation is denoted, " + ODE + ".");
    }

    // driver that calls on the methods above, with user input for the coefficients & initial values

    public static void main(String[] args)
    {
        differentialEquation ODE = new DifferentialEquation(1, 5, 6, 1, Math.PI);

        coefficientDeterminer coefficients = new coefficientDeterminer();

        rootClassifier solution = new rootClassifier();

        System.out.println(solution);
    }
}