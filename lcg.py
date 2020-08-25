#Simple Linear Congruential Generator (LCG)

import numpy as np
import matplotlib.pyplot as plt


def generator(seed, n,):
    #create an empty list to store our n random numbers
  array_of_rn = np.empty(n)

  for i,_ in enumerate(array_of_rn):
    random_number = np.mod((58598 * seed), 233280)
      #save the random number
    array_of_rn[i] = random_number
      #reset the seed to the last random number
    seed = random_number

  return array_of_rn


x = generator(1438786,100)
y = generator(5,100)

plt.scatter(x,y)
plt.title("100 Points on a Good Generator")
plt.show()

#A bad implementation of LCG

def bad_generator(seed, n,):
    #create an empty list to store our n random numbers
  array_of_rn = np.empty(n)

  for i,_ in enumerate(array_of_rn):
    random_number = np.mod((2 * seed), 8)
      #save the random number
    array_of_rn[i] = random_number
      #reset the seed to the last random number
    seed = random_number

  return array_of_rn


x = bad_generator(1438786,100)
y = bad_generator(5,100)

plt.scatter(x,y)
plt.title("100 Points on a Bad Generator")
plt.show()
