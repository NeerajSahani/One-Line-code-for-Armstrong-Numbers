import numpy as np
print([i for i in range(int(input('Enter the range :'))) if i == sum(np.array(list(str(i)), dtype='int')**len(str(i)))])
