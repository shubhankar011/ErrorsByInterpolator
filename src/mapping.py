import matplotlib.pyplot as plt
import numpy as np
import random

def approx_sqrt(i):
    a = int(i**0.5)
    b = ((a+1)**2)-(a**2)
    b = a+((i-a**2)/b)
    return b

def approx_sqrt2(i):
    g = random.randint(1,i)
    while True:
        g = (g + i/g) / 2

        if abs(g*g - i) < 1e-6:
            break
    return g

x_vals = np.arange(4, 17)
y2 = [approx_sqrt2(x) for x in x_vals]
errors = [abs(approx_sqrt(x)) for x in x_vals]
plt.figure(figsize=(15, 9))
plt.plot(errors,x_vals, color='red')
plt.plot(y2,x_vals,color='blue')
plt.title("Analysis of Linear Interpolation")
plt.xlabel("Number (x)")
plt.ylabel("Results")
plt.savefig('Comparison.png')
