import pandas as pd
df = pd.read_csv('al_results_2020.csv', low_memory=False)

transform = df.drop(columns=['Zscore', 'gender', 'syllabus'], axis=1, inplace=True)

transform = df['birth_date'] = df['birth_day'] + ' ' + df['birth_month'] + ' ' + df['birth_year']
print(df)

transform = df.dropna()

transform.to_csv('al_transform.csv')