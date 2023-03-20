import pandas as pd
import random


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

encoded_data = pd.DataFrame(columns=['robot', 'human'])

encoded_data['robot'] = (data['whoAmI'] == 'robot').astype(int)
encoded_data['human'] = (data['whoAmI'] == 'human').astype(int)

encoded_data.head()