#!/usr/bin/python


import numpy as np
from invdisttree import Invdisttree

def  transform_to_uc1(wf1,L):

    a0=0.5431;
    T=wf1.shape[0];

    mu=3 # number of primitive cells considered to form unit cell
    xx = np.linspace(0,mu,T*mu+1)-1
    xx=xx[0:-1]


    x1, y1, z1 = np.meshgrid(xx,xx,xx);

    wf=np.zeros((mu*T,mu*T,mu*T))

    for j1 in xrange(mu):
        for j2 in xrange(mu):
            for j3 in xrange(mu):
                wf[j1*T:((j1+1)*T),j2*T:((j2+1)*T),j3*T:((j3+1)*T)] = wf1


    x=(y1+z1)*0.5*a0;
    y=(x1+z1)*0.5*a0;
    z=(x1+y1)*0.5*a0;

    F = Invdisttree(np.vstack((x.flatten(), y.flatten(), z.flatten())).T, wf.flatten());


    lin = np.linspace(0,a0,L+1)
    lin = lin[0:-1]

    x1 ,y1, z1 = np.meshgrid(lin, lin, lin)

    #% the origin is placed between nodes
    #% x1=x1-0.5*a0/L;
    #% y1=y1-0.5*a0/L;
    #% z1=z1-0.5*a0/L;

    wf = F(np.vstack((x1.flatten(), y1.flatten(), z1.flatten())).T,nnear=11, eps=0, p=1);
    return wf.reshape(x1.shape)
