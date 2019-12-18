# -*- codingXyz_web = {‘day’ : [1,2,3,4,5,6], 
import pandas as pd
xyz_web = {'day' : [1,2,3,4,5,6], 
'visitors': [ 200,2000,10000,6000,
1000,400],'bounce Rate': 
[20,20,23,15,14,10] }
df =pd.DataFrame(xyz_web)
print(df.head(2))
print(df.tail(2))