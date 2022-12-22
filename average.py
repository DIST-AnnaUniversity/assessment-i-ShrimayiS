import pandas as pd
import numpy as np
#read csv file

df = pd.read_csv("iris.csv")

#find the average of petal width

m = np.mean(df["pw"]);

#round off to 2 decimal places

m = round(m,2)

#print only average

print(m)
