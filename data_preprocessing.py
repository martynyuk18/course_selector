import pandas as pd

col_names = ['programs', 'program_spec', 'entrance_tests', 'entrance_tests_1', 'prioraty', 'prioraty_1', 'min_score',
             'min_score_1', 'link', 'link_1', 'empty', 'cost']
data = pd.read_excel('directions.xlsx', names=col_names)

data.entrance_tests = data['entrance_tests'].fillna(data['entrance_tests_1'])
data.prioraty_1 = data['prioraty_1'].fillna(data['min_score'])
data.prioraty = data['prioraty'].fillna(data['prioraty_1'])
data.min_score_1 = data['min_score_1'].fillna(data['link'])
data.min_score = data['min_score'].fillna(data['min_score_1'])

data.iloc[22:108, 6] = data.iloc[22:108, 7]
data.iloc[3, 9] = data.iloc[3, 8]

data.iloc[175:179, 1] = 'Античность(История)'
data.iloc[[3, 16, 50], 2] = 'информатика'

odd_cols = ['entrance_tests_1', 'prioraty_1', 'min_score_1', 'link', 'empty']
for col in odd_cols:
    del data[col]

data.drop(index=[0, 1, 6], inplace=True)

data.programs = data.programs.ffill()
data.program_spec = data.program_spec.ffill()
data.cost = data.cost.ffill()
data.link_1 = data.link_1.ffill()

data = data.dropna()

data.to_csv('data.csv')
