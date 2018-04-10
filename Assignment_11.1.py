import pandas as pd

df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})

df = df.assign(Y=df.loc[df.X==0])

nul = df['Y'].isnull()
df.assign(Y=nul.groupby((nul.diff() == 1).cumsum()).cumsum()).astype("int64")