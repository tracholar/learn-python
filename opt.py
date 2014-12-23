import numpy as np
from scipy.optimize import minimize

def f(x):
	return sum(x ** 2), x
	
	
x = np.random.rand(10)

options = {'maxiter':100, 'disp': True, 'gtol':1e-6}
res = minimize(f,x,method='BFGS', jac=True, options = options)

print res
	
