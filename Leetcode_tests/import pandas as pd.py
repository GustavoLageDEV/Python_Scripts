import pandas as pd

data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

dataframe = pd.DataFrame(data,columns=["Student_id","Age"])



print(dataframe)