--
--  simpleJacobianSolver.hs
--
--  The Jacobian matrix is a functional mapping from Rᵐ → Rⁿ. It is of m x n dimensions and a matrix rep-
--  resentation of a particular function. In this case, the function receives the parameter of three variables
--  and exists in R³. Its entries are constructed from partial derivatives of the defined equation, with
--  respect to each of its input parameters. Ultimately, the program outputs a row vector, 1 x n in dimen-
--  sion. The Jacobian appears in differential geometry and multivariable calculus. It can be applied to 
--  problems resolvable with machine learning techniques. This program, which computes the Jacobian matrix
--  for an equation three variables, has yet to be tested.
--
--_______________________________________________________________________________________________________________



-- defines symbols utilized in the algorithm

Int x y z

let f = xy^2 + 10z



-- instantiates a function that evaluates an a partial derivative w.r.t. certain variables

eval :: [(String, Double)] -> Expr -> Double 

eval_ (Const u) = u

data Expr = Var String

          | Const Double

          | Add Expr Expr

          | Mul Expr Expr

          | Pow Expr Double


eval vars (Var x) = case lookup x vars of 

                    Just v -> v 

                    Nothing -> error ("Variable " ++ x ++ " not found.")


partialDerivatives :: String -> Expr -> Expr 

partialDerivatives x (Const _) = Const 0 

partialDerivatives x (Var y) = if x == then Const 1    

                                else Const 0

partialDerivatives x (Add e1 e2 e3) = Add (partialDerivative x e1) (partialDerivative x e2)

partialDerivatives x (Mul e1 e2 e3) = Add (Mul (partialDerivative x e1) e2) (Mul e1 (partialDerivative x e2))

partialDerivative x (Pow e p) = Mul (Mul (Const p) (Pow e (p - 1))) (partialDerivative x e)



-- calculates a function with respect to the variable of the coordinate axis, x

main :: IO ()

main = do

  let expr = Add (Pow ((Var "x") 1) (Mul (Pow (Var "y") 2))) (10 Var "z") 

  let ∂F/∂x = partialDerivative "x" expr

  putStrLn $ "The partial derivative of f(x, y, z) with respect to x is " ++ show result ++ "."



-- computes the partial derivative of the function with respect to a second variable, y

main :: IO ()

main = do

  let expr = Add (Pow ((Var "x") 1) (Mul (Pow (Var "y") 2))) (10 Var "z") 

  let ∂F/∂y = partialDerivative "y" expr

  putStrLn $ "The partial derivative of f(x, y, z) with respect to y is " ++ show result ++ "."



-- solves for the partial derivative of the differential equation with respect to a third variable, z

main :: IO ()

main = do

  let expr = Add (Pow ((Var "x") 1) (Mul (Pow (Var "y") 2))) (10 Var "z") 

  let ∂F/∂z = partialDerivative "z" expr

  putStrLn $ "The partial derivative of f(x, y, z) with respect to z is " ++ show result ++ "."



-- instantiates an array that describes the Jacobian row vector & adds the PDEs computed above

main :: IO ()

J = array([∂F/∂x, 
           ∂F/∂y,
           ∂F/∂z])



-- prints the Jacobian to the user

print("The final Jacobian row vector is ::", J)
