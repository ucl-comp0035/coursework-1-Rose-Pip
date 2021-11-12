# Write code that prepares your data
# Write code that prepares your data
import pandas as pd

def remove_nan(df):
    """

    Args:
        df: this is the input dataframe to convert NaN values in each column
        to either 0 (int type) if the column is int64 or float64 type,
        or 'not recorded' (string type) if the column is a mixed type or purely string type

    Returns:
        the converted dataframe with no NaN ideally
    """
    type_dict = df.dtypes
    key_list = list(type_dict)
    for i in range(0,len(key_list)):
        if key_list[i] == 'float64' or key_list[i] == 'Int64':
            df.iloc[:, i] = df.iloc[:, i].replace(np.nan, 0)
        else:
            df.iloc[:, i] = df.iloc[:, i].replace(np.nan, 'not recorded')
    return df

if __name__ == '__main__':
    '''
    df_2021 is the recorded data in 2021 
    df_2018 is the recorded data in 2018
    '''
    df_2021 = pd.read_csv(r'data/Borough_tree_list_2021.csv', low_memory=False)
    print(df_2021)  # to visualise the raw data of trees ditribution recorded in 2021
    # .drop(columns=) drops the columns not needed for data exploration or empty ones
    df_cl_21 = df_2021.drop(columns=['taxon_name', 'lon', 'lat', 'load_date', 'objectid', 'gdb_geomattr_data'])
    df_cl_21_f = remove_nan(df_cl_21)
    print(df_cl_21_f)
    df_21 = df_cl_21_f.to_csv('prepared_data/df_21.csv')


    df_2018=pd.read_excel(r'data/london_street_trees_gla_20180214.xlsx')
    print(df_2018) # to visualise the raw table of trees distribution in 2018
    # .drop(columns=) drops the columns not needed for data exploration or empty ones
    df_cl_18=df_2018.drop(columns=['gla_id','common_name', 'easting', 'northing', 'longitude', 'latitude'])
    df_cl_18_f=remove_nan(df_cl_18)
    df_18=df_cl_18_f.to_csv('prepared_data/df_18.csv')




