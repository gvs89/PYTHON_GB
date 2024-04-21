import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

categories = data['whoAmI'].unique()
one_hot = pd.DataFrame(columns=categories)
for index, row in data.iterrows():
    category = row['whoAmI']
    one_hot.loc[index, category] = 1
print(one_hot)