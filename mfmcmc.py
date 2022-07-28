import numpy as np
import random as r


def mcmc(func,prior,X,y,guess,risk,step,iter,burn):
## This function uses a Metropolis-Hastings algorithm in order
## to optimize the fit parameters. It returns the optimal 
## parameters as well as histograms describing the parameter space

	## Set up relevant MCMC parameters
	#### T is the number of iterations. ncut is the burn in.
	#### delta is the maximum jump size; i.e. step size. 	
	T = iter
	ncut = burn
	delta = step
	
	## Find number of parameters
	par = len(guess)

	accept = 0

	## Initialize the parameters
	theta = np.zeros((par,T))
	theta[:,0] = guess	
	
	## Loop for the desired number of iterations
	for i in range(T-1):
		
		## Copy over value
		theta[:,i+1] = theta[:,i]
		
		## Get random numbers to perturb and check
		u = np.random.rand(par)
		utest = np.random.rand(1)
	
		## Perturb
		theta[:,i+1] += delta*(2*u-1)
		
		## Get change
		new = getP(theta[:,i+1],data,polymer,j,guess,sigy)
		old = getP(theta[:,i],data,polymer,j,guess,sigy)
		diff = new / old	

		if utest <= diff:	
			pass
			accept += 1
		else:
			theta[:,i+1] = theta[:,i]
		
	theta = theta[:,ncut:]
	
	## Finally, collect the output parameters
	t_mc = np.zeros(2,num_of_scans)	
	print("Select the best fit parameters, with Enter in between: ")
	t_mc[0,j] = float(input())
	t_mc[1,j] = float(input())
	
	## A good acceptance rate is 0.25-0.4
	print("Acceptance rate: ", accept / (T*num_of_scans))
	
	return t_mc	


