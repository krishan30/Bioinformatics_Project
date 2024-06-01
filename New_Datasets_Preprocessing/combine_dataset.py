import pandas as pd

# List of file paths for your CSVs
csv_files = ['Preprocessed_Datasets/Deeploc1.0/deeploc_data_sub_part_1_include.csv','Preprocessed_Datasets/Deeploc1.0/deeploc_data_sub_part_2_include.csv', 'Preprocessed_Datasets/Deeploc1.0/deeploc_data_sub_part_3_include.csv', 'Preprocessed_Datasets/Deeploc1.0/deeploc_data_sub_part_4_include.csv', 'Preprocessed_Datasets/Deeploc1.0/deeploc_data_sub_part_5_include.csv']

# Initialize an empty list to hold DataFrames
dfs = []

# Read each CSV file and append its DataFrame to the list
for file in csv_files:
    df = pd.read_csv(file)
    dfs.append(df)

# Concatenate all DataFrames in the list along rows (axis=0)
combined_df = pd.concat(dfs, ignore_index=True)
combined_df.to_csv('Combined_Dataset/deeploc_combined_data.csv', index=False)
# Print the combined DataFrame
print(combined_df)
