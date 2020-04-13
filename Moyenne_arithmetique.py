#%% IMPORT PACKAGES

import numpy as np
import pandas as pd



#%% CREATE OBJECTS

x = [1, 2, 3]  

x = pd.Series(data = x,
              name = 'x')   # Convert list into column vector 

n = len(x)                  



#%% COMPUTE

# Option 1

1/n * sum(x)



# Option 2 

np.mean(x)                 



