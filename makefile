# Makefile for building AMICA test program

# Compiler (using mpif90 wrapper to handle MPI + Fortran)
FC       = mpif90

# Compiler flags
FFLAGS   = -cpp -fopenmp -ffree-form -ffree-line-length-none

# Libraries to link
LIBS     = -lblas -llapack

# Sources and target
SRC      = funmod2.f90 amica15.f90
TARGET   = amica15ub_test

# Default rule
all: $(TARGET)

$(TARGET): $(SRC)
	$(FC) $(FFLAGS) $(SRC) $(LIBS) -o $(TARGET)

# Clean rule
clean:
	rm -f $(TARGET) funmod2.o funmod2.mod
