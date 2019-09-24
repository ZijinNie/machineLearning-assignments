# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 17:35:50 2019

@author: Frankenstein Nie
"""
import numpy as np
class LDA:
    
    def fit(self, X, Y):
        n0=0
        n1=0
        X0sum= np.zeros((X.shape[1],1))
        X1sum= np.zeros((X.shape[1],1))
        covariance = np.zeros((X.shape[1],X.shape[1]))
        
        for i in range(X.shape[0]):
            if (Y[i] == 1):
               # print("111")
                n1+=1
                X1sum=np.add(X1sum, np.array([X[i, :]]).T) 
            else:
                #print("000")
                n0+=1
                X0sum=np.add(X0sum, np.array([X[i, :]]).T)
        
        
        p0= n0/(n0+n1)
        p1= n1/(n0+n1)
        


        u0= np.divide(X0sum,n0)
        u1= np.divide(X1sum,n1)
        
        for j in range(X.shape[0]):
            if Y[j] == 0:
                delta = np.subtract(np.array([X[j, :]]).T, u0)
                covariance = np.add(covariance, np.dot(delta,delta.T))
            else:
                delta = np.subtract(np.array([X[j, :]]).T, u1)
                covariance = np.add(covariance, np.dot(delta,delta.T))
        
        covariance = np.divide(covariance,n0+n1-2)
        '''
        print(u0)
        print(u1)
        print(p0)
        print(p1)
        print(covariance)
        '''
        return p0, p1, u0, u1, covariance
    
    def predict (self, x, u0, u1, p0, p1,covariance):
        y = np.zeros(x.shape[0])
        for i in range(x.shape[0]):
            log_odds = np.log(p1/p0) - 0.5*np.dot(np.dot(u1.T,np.linalg.inv(covariance)),u1)+ 0.5*np.dot(np.dot(u0.T,np.linalg.inv(covariance)),u0)+np.dot(np.dot(x[i].T,np.linalg.inv(covariance)), (u1-u0))
            if log_odds >0.5:
                y[i] = 1
            else:
                y[i] = 0
        return y
    
    
        
        
        