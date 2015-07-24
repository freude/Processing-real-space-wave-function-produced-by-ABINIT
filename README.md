# Reading-grid-wave-functions-produced-by-ABINIT-
This software operates with ABINIT output data stored in netCDF files. The software converts a wave functions computed on a grid in a primitive cell to the wave functions specified on a user-defined grid in a unit cell. The core of the program is kdtree intepolation tool implemented in python by https://github.com/thouis/align/blob/master/freak/invdisttree.py

To operate netCDF files produced by ABINIT in python, the latest version of netcdf4-python should be installed.

The problem to be solved is illustrated in the figure below.

![alt tag](https://github.com/freude/Reading-grid-wave-functions-produced-by-ABINIT-/blob/master/drawing.png)

