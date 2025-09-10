import pandas as pd

data={'company':['goog','Good','MSFT','MSFT','FB','FB'],
      'Person':['Sam','Charlie','Amy','Vanessa','Car','Sarah'],
      'Sales':[200,120,320,456,124,250]}

df=pd.DataFrame(data)
print(df)

by_comp=df.groupby('company')
print(by_comp)

print(by_comp.mean())
print(by_comp.max())
print(by_comp.min())
