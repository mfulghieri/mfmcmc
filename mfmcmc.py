import numpy as np
import random as r


def mcmc(data, polymer, num_of_scans):
## This function uses a Metropolis-Hastings algorithm in order
## to optimize the fit parameters. It returns the optimal 
## parameters as well as histograms describing the parameter space

	## Obtain initial guess
	print("Provide guess for thickness and scaling, with Enter in between: ")
	dguess = float(input())
	aguess = float(input())
	guess = dguess,aguess	

	## Set up y errors
	sigy = 0.25

	## Set up relevant MCMC parameters
	#### T is the number of iterations. ncut is the burn in.
	#### delta is the maximum jump size; i.e. step size. 	
	T = 30000
	ncut = 5000
	delta = [100,0.1]

	accept = 0

	for j in range(num_of_scans):

		## Initialize the parameters
		theta = np.zeros((2,T))
		theta[:,0] = guess	
		
		## Loop for the desired number of iterations
		for i in range(T-1):

			## Copy over value
			theta[:,i+1] = theta[:,i]
			
			## Get random numbers to perturb and check
			u = np.random.rand(2)
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
	

		## Print out the median values for assistance
		print("Median for d = {0} ## Caution: may not work for multimodal output".format(np.around(np.median(theta[0,:]),1)))	
		print("Median for a = {0} ## Caution: may not work for multimodal output".format(np.around(np.median(theta[1,:]),1)))
	
		## Plot 1d histograms and quality assurance
		names = ["d","a"]
		xaxes = ["Thickness (nm)","Scaling Factor (au)"]
		
		for k in range(2):
			plt.subplot(2,2,k+1)
			plt.hist(theta[k,:],bins=35)
			plt.title("MCMC Samples for {0}".format(names[k]))
			plt.xlabel(xaxes[k])
			plt.ylabel("Counts")

			plt.subplot(2,2,k+3)
			plt.plot(theta[k,:],np.arange(ncut,T),linestyle='-',color='black',linewidth=1.0)
			plt.title("Quality Assurance for {0}".format(names[k]))
			plt.xlabel(names[k])
			plt.ylabel("Iteration #")

		plt.tight_layout()

		## Plot 2d histogram 
		plt.figure()
		plt.hist2d(dlist,alist,bins=100)
		plt.show()
			
		## Finally, collect the output parameters
		t_mc = np.zeros(2,num_of_scans)	
		print("Select the best fit parameters, with Enter in between: ")
		t_mc[0,j] = float(input())
		t_mc[1,j] = float(input())
	
	## A good acceptance rate is 0.25-0.4
	print("Acceptance rate: ", accept / (T*num_of_scans))
	
	return t_mc	


