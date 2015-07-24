#!/usr/bin/python
"""The module of the class  UTable """

import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from transform_to_uc1 import transform_to_uc1

def read_wf(T, k1, f_name):

    if k1[0]!=0.0:
        if k1[0]>0.0:
            indi=4
        if k1[0]<0.0:
            indi=5

    if k1[1]!=0.0:
        if k1[1]>0.0:
            indi=1
        if k1[1]<0.0:
            indi=3

    if k1[2]!=0.0:
        if k1[2]>0.0:
            indi=0
        if k1[2]<0.0:
            indi=2


    f = Dataset(f_name)

    wf_r=f.variables["real_space_wavefunctions"][0,indi,4,0,:,:,:,0]
    wf_i=f.variables["real_space_wavefunctions"][0,indi,4,0,:,:,:,1]

    wfr=transform_to_uc1(wf_r,T);
    wfi=transform_to_uc1(wf_i,T);

    return wfr+1j*wfi

if __name__ == "__main__":

    k1=np.array([1,0,0])
    w=read_wf(50,k1,"/data/users/mklymenko/abinitio_software/abi_files/tpaw/tbase3_xo_DS2_AE_WFK-etsf.nc")

    x=np.linspace(0,1,50)
    xi, yi = np.meshgrid(x, x)

    w = np.abs(w)

    plt.contour(xi, yi, w[:,:,0], colors='red')
    plt.hold(True)
    plt.show()
