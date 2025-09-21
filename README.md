# Dev Branch for AMICA Testing (Not for general use)

This branch is for development and testing of the AMICA algorithm and its Python
implementation. It is not intended for general use. Namely, this branch has an updated
version of the Fortran AMICA code that fixes the random seed initialization to allow
reproducible results, and additionally saves the initial Wtmp, sbetatmp, and mutmp
matrices to allow initializing the Python code with the same values.

To compile the Fortran code, you can use the provided Makefile:

```bash
make
```

Which is the same as running:

```bash
mpif90 -cpp -O0 -g -fopenmp -ffree-form -ffree-line-length-none -lblas -llapack -o amica15_fork_debug amica15.f90
```

To download and run a test data set, you can use the following commands:

```bash
make testdata
```

```bash
make test # Same as: ./amica15ub_test amicadefs_test.param
```

Executing the test will produce an output folder `amicaout_test` containing the results
of the AMICA run.

_________________________________________________________________________________________

![Screenshot 2024-07-25 at 14 12 51](https://github.com/user-attachments/assets/e5880f21-51ae-4ebf-a3de-bc040d6f4aab)

# The AMICA algorithm and EEGLAB plugin

Adaptive Mixture Independent Component Analysis (AMICA) is a program (for Linux, Mac, and Windows) that performs an independent component analysis (ICA) decomposition on input data, potentially with multiple ICA models. It can be run standalone, or from MATLAB.

Code for AMICA: Adaptive Mixture ICA with shared component

Refer to the [Amica wiki](https://github.com/japalmer29/amica/wiki) for documentation or the other menus if you are on the EEGLAB website.

Refer also to Jason Palmer's [AMICA page](https://sccn.ucsd.edu/~jason/amica_web.html).

# Version history

1.7 - Update documentation for pop_runamica and add test file

1.6.1 - Modify Windows compilation instructions. Intel OneAPI should be tested for Mac and Ubuntu.

1.6 - Deprecate Comet and replace with Expanse supercomputer executable

1.5.2 - Comet supercomputer executable

