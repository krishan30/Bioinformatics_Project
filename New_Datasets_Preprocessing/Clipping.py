import pandas as pd


def clip_middle(x, clip_len):
    if len(x) > clip_len:
        x = x[:clip_len // 2] + x[-clip_len // 2:]
    return x


combined_dataset_deeploc = pd.read_csv('deeploc_combined_data_with_partition.csv')
# max_length = combined_dataset_deeploc['Sequence'].apply(len).max()
combined_dataset_deeploc["Sequence"] = combined_dataset_deeploc["Sequence"].apply(lambda x: clip_middle(x, 1022))
combined_dataset_deeploc.to_csv('deeploc_combined_data_1kclipped.csv', index=False)
