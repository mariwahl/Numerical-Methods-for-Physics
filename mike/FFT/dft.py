import math
import numpy
import pylab


def dft(f_n):
    """ perform a discrete Fourier transform.  We use the same
        conventions as NumPy's FFT"""
    
    N = len(f_n)

    # allocate space for the frequency components -- they are, in general,
    # complex
    f_k = numpy.zeros( (N), dtype=numpy.complex128)

    k = 0
    while k < N:
        
        # create f_k by looping over all the f_n real-space data points
        # this will create a complex number 

        n = 0
        while n < N:

            f_k[k] += f_n[n]*numpy.exp(-2.0*math.pi*1j*n*k/N)
            n += 1

        k += 1

    return f_k


npts = 50

f_0 = 0.2

xmax = 50.0
xx = numpy.linspace(0.0, xmax, npts, endpoint=False)

f_n = numpy.sin(2.0*math.pi*f_0*xx)

f_k = dft(f_n)

print f_k[0]

# compute k
k = numpy.arange(npts)/xmax

pylab.plot(k, f_k.real, label="Re(F(k))")
pylab.plot(k, f_k.imag, ls=":", label="Im(F(k))")
pylab.legend(frameon=False, fontsize="small")
pylab.savefig("dft.png")

