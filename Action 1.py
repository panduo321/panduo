import numpy as np

numbers = (np.arange(0,101,2))
sum = 0
for number in numbers:
    sum = sum + number

print(sum)
