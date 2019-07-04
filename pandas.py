"@author: @everydaycodings"
"Accessing a multiple element using index label"

from pandas import Series
import numpy as np 

# creating simple array 
data = np.array(['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's']) 
ser = Series(data, index =[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])


# accessing a multiple element using 
# index element 
print(ser[[10, 11, 12, 13, 14]]) 
