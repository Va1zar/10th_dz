# Задание 44
# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head() |


import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
# print(data.head())

# решение через get_dummies
new_data = pd.get_dummies(data['whoAmI'])
print(new_data.head())

# решение без get_dummies
data.loc[data['whoAmI'] == 'robot', 'robot'] = 1
data.loc[data['whoAmI'] != 'robot', 'robot'] = 0
data.loc[data['whoAmI'] == 'human', 'human'] = 1
data.loc[data['whoAmI'] != 'human', 'human'] = 0
new_data = data[['human', 'robot']]
print(new_data.head())
