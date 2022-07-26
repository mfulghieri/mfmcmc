Hello.

mfmcmc stands for Matteo Fulghieri's Monte Carlo Markov Chain. 

This code is a truly basic Monte Carlo code, meant to be used qualitatively. Least squares is limited because it fails to recognize secondary fits that may be more accurate to the model, but suffer from a lower frequentist probability. In these instances, you might be tempted to guess and check to get a visually correct fit. Instead, you can use this code to do the guess and checking for you. If not at least this, you can use it for. framework for your own MCMC project. 

I will also provide here the documentation for my home-made Monte Carlo. 

mfmcmc(func,prior,X,y,guess,risk,step,iter,burn):

  Inputs:
      
      func(X,A): the model function to be used
        X is the independent variable. You can store more than just one. For example:
        X = x,n where x is the wavelength of light and n is the wavelength dependent index of refraction
        In this case, you would call the varaibles by mfmcmc(func,prior,(x,n),y)
        A is the parameter. Similarly, you can store more than just one by also using a tuple. 
        
      prior(A,guess): the prior distributions to use
        A is the current parameter being loooked at. guess is the inital parameter. If guess is not used
        within prior, still include in the argument. It is included in case you may want to have your parameter space
        investigated around the initial guess. For example: p(A) = scipy.stats.norm( (A[0] - guess[0]) / sigma )
        
      X: the independent variable in the data set
        As previously mentioned, X can be more than just one variable. See above explanation in func(X,A).
        For example, you could have P = nRT/V where X = (n,T,V)
        
      y: the dependent (output) variable in the data set
        This must be a singular output value. For example, you could have P = nRT/V, where y = P
        
      guess: the initial guess for your parameter
        This should match the size of A, and make sure to align the order of the values with that of A.
        
      risk: how risky the stepper should be
     
      step: the step size for each parameter
        This should match the size of A, and make sure to align the order of the values with that of A. 
        The step size should match the scale of the paramter space. 
      
      iter: number of iterations to perform. 
      
      burn: how many iterations to exclude
      
      
        
  Outputs:
    
     mfmcmc: object with several properties
      mfmcmc.chain is the Markov Chain, where each row corresponds to a parameter, and the columns are 
      the different iterations. This can be used to produce both histograms and walks. 
      
      mfmcmc.theta is the estimated best parameters. Be mindful, however, because it is often best to
      interpret yourself. This code is not sophisticated and struggles with multimodal instances
      
      
      
