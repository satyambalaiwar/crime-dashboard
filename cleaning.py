import pandas as pd
import numpy as np

df_raw = pd.read_csv("human_trafficking.csv")
df = df_raw.drop(columns=['Sl. No.'])

df_melted = df.melt(id_vars='State/UT', var_name='YEAR', value_name='CASES_REPORTED')
df_melted['YEAR'] = df_melted['YEAR'].str.extract(r'(\d{4})').astype(int)
df_melted.rename(columns={'State/UT': 'STATE'}, inplace=True)
df_melted['CASES_REPORTED'] = df_melted['CASES_REPORTED'].fillna(0).astype(int)

state_population = {
    'Andhra Pradesh': 53900000,
    'Arunachal Pradesh': 1570000,
    'Assam': 35600000,
    'Bihar': 124800000,
    'Chhattisgarh': 29400000,
    'Goa': 1540000,
    'Gujarat': 70400000,
    'Haryana': 28800000,
    'Himachal Pradesh': 7400000,
    'Jharkhand': 38900000,
    'Karnataka': 67500000,
    'Kerala': 35600000,
    'Madhya Pradesh': 85300000,
    'Maharashtra': 124700000,
    'Manipur': 3300000,
    'Meghalaya': 3200000,
    'Mizoram': 1200000,
    'Nagaland': 2200000,
    'Odisha': 46300000,
    'Punjab': 30100000,
    'Rajasthan': 81000000,
    'Sikkim': 670000,
    'Tamil Nadu': 77300000,
    'Telangana': 39100000,
    'Tripura': 4100000,
    'Uttar Pradesh': 240000000,
    'Uttarakhand': 11200000,
    'West Bengal': 99200000,
    'Delhi': 19800000,
    'Jammu and Kashmir': 13400000,
    'Ladakh': 300000,
    'Andaman and Nicobar Islands': 430000,
    'Dadra and Nagar Haveli and Daman and Diu': 585000,
    'Chandigarh': 1150000,
    'Puducherry': 1600000
}

df_pop = pd.DataFrame(list(state_population.items()), columns=['STATE', 'POPULATION'])
df_final = df_melted.merge(df_pop, on='STATE', how='left')
df_final['HTRS'] = (df_final['CASES_REPORTED'] / df_final['POPULATION']) * 100000

missing_pop_states = df_final[df_final['POPULATION'].isna()]
if not missing_pop_states.empty:
    print("Missing population data for these states:")
    print(missing_pop_states['STATE'].unique())

df_final.to_csv("human_trafficking_cleaned.csv", index=False)
print("Cleaned file saved as 'human_trafficking_cleaned.csv'")
