import pandas as pd

# Load the raw data
df_raw = pd.read_csv("human_trafficking.csv")

# Drop serial number column
df = df_raw.drop(columns=['Sl. No.'])

# Reshape the data
df_melted = df.melt(id_vars='State/UT', var_name='YEAR', value_name='CASES_REPORTED')
df_melted['YEAR'] = df_melted['YEAR'].str.extract(r'(\d{4})').astype(int)
df_melted.rename(columns={'State/UT': 'STATE'}, inplace=True)
df_melted['CASES_REPORTED'] = df_melted['CASES_REPORTED'].fillna(0).astype(int)

# Dummy population data (replace with actual if available)
state_population = {
    'STATE': [
        'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh',
        'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand',
        'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
        'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab',
        'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura',
        'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Delhi', 'Jammu & Kashmir'
    ],
    'POPULATION': [
        53900000, 1570000, 35600000, 124800000, 29400000,
        1540000, 70400000, 28800000, 7400000, 38900000,
        67500000, 35600000, 85300000, 124700000, 3300000,
        3200000, 1200000, 2200000, 46300000, 30100000,
        81000000, 670000, 77300000, 39100000, 4100000,
        240000000, 11200000, 99200000, 19800000, 13400000
    ]
}

df_pop = pd.DataFrame(state_population)

# Merge and compute HTRS
df_final = df_melted.merge(df_pop, on='STATE', how='left')
df_final['HTRS'] = (df_final['CASES_REPORTED'] / df_final['POPULATION']) * 100000

# Save the file
df_final.to_csv("human_trafficking_cleaned.csv", index=False)
