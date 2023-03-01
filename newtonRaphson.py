
def newtonRaphson(g, x0, eps, delta, itermax):
    print("Please fill in this function")

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


