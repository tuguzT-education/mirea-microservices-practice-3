import numpy as np
from pprint import pprint

n = int(input('Enter array length: '))
result = np.random.random(n)
print(f'Random array of length {n}:')
pprint(list(result))
