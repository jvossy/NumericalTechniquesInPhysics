# Jacob Vosburgh
import numpy as np
def calculateSum_16bit(delta):
    sum = np.float16(0.0)
    delta = np.float16(delta)  # Convert delta to a 16-bit floating point number.

    if delta == np.float16(0.0):  # If the 16-bit representation is exactly zero, throw an error.
        print("Error: delta = " + str(delta) + " is equal to zero at this precision of 16 bits.")
        return

    for i in range(0, int(round(1.0 / delta))):  # Compute the sum using a for loop.
        sum += delta
    return sum

def calculateSum_32bit(delta):
    sum = np.float32(0.0)
    delta = np.float32(delta)  # Convert delta to a 32-bit floating point number.

    if delta == np.float32(0.0):  # If the 32-bit representation is exactly zero, throw an error.
        print("Error: delta = " + str(delta) + " is equal to zero at this precision of 32 bits.")
        return

    for i in range(0, int(round(1.0 / delta))):  # Compute the sum using a for loop.
        sum += delta
    return sum

def calculateSum_64bit(delta):
    sum = np.float64(0.0)
    delta = np.float64(delta)  # Convert delta to a 64-bit floating point number.

    if delta == np.float64(0.0):  # If the 64-bit representation is exactly zero, throw an error.
        print("Error: delta = " + str(delta) + " is equal to zero at this precision of 64 bits.")
        return

    for i in range(0, int(round(1.0 / delta))):  # Compute the sum using a for loop.
        sum += delta
    return sum
#--------------------------------
x1 = .1
print("Delta = 10^-1")
print("16-bit " + str(calculateSum_16bit(x1)))
print("32-bit " + str(calculateSum_32bit(x1)))
print("64-bit " + str(calculateSum_64bit(x1)))
x2 = .01
print("Delta = 10^-2")
print("16-bit " + str(calculateSum_16bit(x2)))
print("32-bit " + str(calculateSum_32bit(x2)))
print("64-bit " + str(calculateSum_64bit(x2)))
x3 = .001
print("Delta = 10^-3")
print("16-bit " + str(calculateSum_16bit(x3)))
print("32-bit " + str(calculateSum_32bit(x3)))
print("64-bit " + str(calculateSum_64bit(x3)))
x4 = .0001
print("Delta = 10^-4")
print("16-bit " + str(calculateSum_16bit(x4)))
print("32-bit " + str(calculateSum_32bit(x4)))
print("64-bit " + str(calculateSum_64bit(x4)))
x5 = .00001
print("Delta = 10^-5")
print("16-bit " + str(calculateSum_16bit(x5)))
print("32-bit " + str(calculateSum_32bit(x5)))
print("64-bit " + str(calculateSum_64bit(x5)))
