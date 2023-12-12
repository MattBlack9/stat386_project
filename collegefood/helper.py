import pandas as pd 
import seaborn as sns
import numpy as np
import regex as re
import matplotlib.pyplot as plt


def drop_columns(dataframe, columns_to_drop):
    """
    Drops specified columns from a DataFrame.

    Parameters:
        dataframe (pd.DataFrame): The input DataFrame.
        columns_to_drop (list): List of column names to be dropped.

    Returns:
        pd.DataFrame: DataFrame with specified columns dropped.
    """
    dataframe = dataframe.drop(columns=columns_to_drop, errors='ignore')
    return dataframe

def cleaning_col(column,type,data):
    """
    Converts specified column to new data type and deleting observations that do not apply

    Parameters:
        column (string): The column that needs to be edited
        type (data type): The data type that is desired
        data (pd.DataFrame): The DataFrame that is needing to be changed

    Returns:
        pd.DataFrame: DataFrame with correct column type
    """
    my_array = []
    for i in data[column]:
        try:
            temp = type(i)
            my_array.append(temp)
        except ValueError:
            temp = np.nan
            my_array.append(temp)
    data[column] = my_array