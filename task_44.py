# Задача 44: В ячейке ниже представлен код генерирующий DataFrame,
# которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид.
# Сможете ли вы это сделать без get_dummies?

# import random
# import pandas as pd

# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

# pd.get_dummies(data)

import numpy as np
import pandas as pd

hotlike =  np.random.randint(0,1,size=(10,2))
hotlike = pd.DataFrame(data, columns=['human', 'robot'])

print(hotlike)

df = pd.DataFrame({'human': [0,0,0,0,0], 'robot': [0,0,0,0,0]})


for i in range(len(df)):
    df.loc[i,'human'] = 0 
    df.loc[i, 'robot'] = 0 

    
display(df)


