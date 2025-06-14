import pandas as pd

df = pd.read_csv("human_trafficking_cleaned.csv")
df.head()
import matplotlib.pyplot as plt
import seaborn as sns

print(df.columns)
print(df['STATE'].nunique())   # how many unique states
print(df['YEAR'].min(), df['YEAR'].max())   # year range
df.describe()

state_scores = df.groupby('STATE')['HTRS'].mean().reset_index().sort_values(by='HTRS', ascending=False)

yearly_trend = df.groupby('YEAR')['HTRS'].mean().reset_index()
plt.figure(figsize=(12, 6))
sns.barplot(data=state_scores, x='HTRS', y='STATE', palette='viridis')
plt.show()