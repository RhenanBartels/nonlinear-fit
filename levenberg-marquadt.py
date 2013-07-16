#_*_ coding: utf-8 _*_

import numpy as np

def lm(func, p, t, y_dat, weigth, dp, p_min, p_max, c):
    """
         func -> function of n independent variables, 't', and m parameters 'p'
         p -> n-vector of initial guess of parameter values.
         t -> m-vectors or matrix of idenpendet variables
         y_dat -> m-vectors or matrix of data to be fit by func(t, p)
         weith -> wieghting vector for least squares fit (weight >=0)
         dp -> fractional increment of 'p' for numerical derivatives
         p_min -> n-vector of lower bounds for parameters values.
         p_max ->n-vector of upper bounds for parameters values.
    """

    p = p.T  #Must be a column vector
    y_dat = y_dat.T # Must be a column vector
    Npar = len(p)
    Npnt = len(y_dat)

    if Npar != Npnt:
        raise Exception("the length of t must be equal the length of y_                        dat")

    MaxIter = 20 * Npar
    epsilon_1 = 1e-3  #convergence tolerance for gradient
    epsilon_2 = 1e-3  #convergence tolerance for parameters
    epsilon_3 = 1e-3  #convergence tolerance for chi_square
    epsilon_4 = 1e-2  #determines acceptance of L-M step
    lamba_0 - 1e-2  #initial value of damping parameter, lamba
    lambda_UP_fac = 11  #factor for increasing lambda
    lambda_DN_fac = 9  # factror for decreasing lambda
    Update_Type = 1

    weight = np.sqrt((Npnt - Npar + 1) / (sum(y_dat**2)))
    dp = 0.001
    p_min = -100 * abs(p) #ja é vetor coluna
    p_max = 100 * abs(p)  #ja é vetor coluna

    if len(dp) == 1:
        dp = dp * np.ones((Npar, 1))
    idx = np.where(dp != 0)[0] #indices of the parameters to be fit
    Nfit = len(idx)
    stop = 0  #termination flag

    weigth_sq = weigth * np.ones((Npnt, 1))**2




