import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("human_trafficking_cleaned.csv")

state_scores = df.groupby('STATE')['HTRS'].mean().reset_index().sort_values(by='HTRS', ascending=False)

plt.figure(figsize=(14, 8))
sns.barplot(data=state_scores, x='HTRS', y='STATE', palette='viridis')

plt.title("Average Human Trafficking Rate Score by State (India)", fontsize=16, fontweight='bold')
plt.xlabel("Average HTRS", fontsize=12)
plt.ylabel("State", fontsize=12)
plt.suptitle("Data Source: human_trafficking_cleaned.csv | Visualization: Seaborn & Matplotlib", fontsize=10, y=0.93, color='gray')
plt.tight_layout()
plt.show()

#adding this to checking commit problem