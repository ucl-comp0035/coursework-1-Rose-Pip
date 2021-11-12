# Write code that prepares your data
import pandas as pd
import numpy as np

if __name__ == '__main__':
    '''
    df_2021 is the recorded data in 2021 
    df_2018 is the recorded data in 2018
    '''
    df_2021 = pd.read_csv(r'data/Borough_tree_list_2021.csv', low_memory=False)
    print(df_2021.head(5))  # to visualise the raw data of trees ditribution recorded in 2021
    # spot empty cells and columns
    print(np.where(pd.isnull(df_2021)))
    #spot the type of values in each column
    print(df_2021.dtypes)


    df_2018 = pd.read_excel(r'data/london_street_trees_gla_20180214.xlsx')
    print(df_2018.head(5))   # to visualise the raw table of trees distribution in 2018
    # spot empty cells and columns
    print(np.where(pd.isnull(df_2018)))
    # spot the type of values in each column
    print(df_2021.dtypes)
