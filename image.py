import numpy as np
from PIL import Image as im
  
arr = []
for i in range(4096):
    for j in range(4096):
        arr.append((i + j) // (2 * 4 * 4))
    
array = np.array(arr, dtype=np.uint8)
print(type(array))
print(array.shape)
array = np.reshape(array, (4096, 4096))
print(array.shape)
print(array)
data = im.fromarray(array)
data.save('gradient.png')
