# saveAUTOresults

Python script for scanning for periodic solution of system of ODEs using [AUTO numerical continuation package](http://cmvl.cs.concordia.ca/auto/). The results are saved in HDF5 file using [deepdish.io](http://deepdish.readthedocs.io/en/latest/io.html) Python package.

The skelton.c is the equation file, and c.skelton is the continuation parameters file. Use AUTO documentation to edit those file for the specific ODE system under study.

After the above files are set, by importing scan.py from within the AUTO shell, the numerical continuation is performed using `bif=scan.scanBif('string-name-of-equantion-and-parameters-file')`.
