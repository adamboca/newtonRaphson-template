
def newtonRaphson(g, x0, eps, delta, itermax):
    x_old = x0
    for i in range(itermax):
        func = g(x_old)
        x_new = x_old - func[0]/func[1]
        if abs(x_new-x_old) < eps:
           print("The solution converged.")
           break
        if abs(x_new-x_old) > delta:
           print("The solution diverged.")
           break
        x_old = x_new
    return x_new

# This is an example function to be passed to newtonRaphson
def example_function(x):
  f = pow(x, 2) - 1
  fx = 2*x
  return f, fx

# This main statement contains some examples calling the newtonRaphson
if __name__ == '__main__':
    # This is a simple example that is expected to find a root
    root = newtonRaphson(example_function, 1.5, 1E-8, 1E2, 100)
    print("The found root is ", root)


