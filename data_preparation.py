# Write code that prepares your data
# Write code that prepares your data
import pandas as pd 
import numpy as np 
if __name__=='__main__':
    '''
    df_2021 is the recorded data in 2021 
    df_2018 is the recorded data in 2018
    '''
    df_2021=pd.read_csv(r'https://github.com/ucl-comp0035/coursework-1-Rose-Pip/tree/master/data/Borough_tree_list_2021.csv', low_memory=False)
    display(df_2021) # to visualise the raw table of trees ditribution recorded in 2021 
    df_cl_21=df_2021.drop(columns=['taxon_name','lon','lat','load_date','objectid','gdb_geomattr_data','diameter_at_breast_height_cm'])
    display(df_cl_21)
    
    df_2018=pd.read_excle(r'https://github.com/ucl-comp0035/coursework-1-Rose-Pip/tree/master/data/london_street_trees_gla_20180214.xlsx')
    display(df_2018) # to visualise the raw table of trees distribution in 2018
    df_cl_18=df_2018.drop(columns=['longtitude','latitude','easting','northing','longitude','latitude'])
    df_pre_21=df_cl_21.to_csv(r'https://github.com/ucl-comp0035/coursework-1-Rose-Pip/tree/master/data/Borough_tree_list_2021_cleaned.csv')
