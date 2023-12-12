import pandas as pd 
import seaborn as sns
import numpy as np
import regex as re
import matplotlib.pyplot as plt

def to_vector_of_strings(dataframe, column_name):
    """
    Converts all the strings in a dataset's column into a vector of strings. Useful if there are multiple strings in a single row.

    Parameters

        dataframe: The dataframe you want to perform the function on

        column_name: The column in the dataframe to perform the fuction on
    

    Returns

        An array of all the strings that are every row of the column

    """
    # Split words using commas and periods
    words_list = dataframe[column_name].str.lower().str.replace('.', ',').str.split(',').explode().str.strip().tolist()
    # Create a new DataFrame with a row for each word
    vector_of_words = pd.DataFrame({
        '{}_word'.format(column_name): words_list
    })
    
    return vector_of_words



def replace_with_synonym(dataframe, column_name, words_to_replace):
    """
    This function uses a dictionary of synonyms to combine similar words.

    Parameters:

        dataframe: The dataframe you want to perform the function on

        column_name: The column in the dataframe to perform the fuction on

        words_to_replace: A dictionary with the words you want to replace. Format is 'word_to_be_replace' : 'replacement_word'

    Returns

        This function returns a dataframe with the replaced values.

    """
    # Replace words using the specified mapping
    for original_word, replacement_word in words_to_replace.items():
        dataframe[column_name] = dataframe[column_name].replace(original_word, replacement_word)

    # Group and sum the occurrences of each word
    grouped_data = dataframe.groupby(column_name, as_index=False).sum()

    return grouped_data

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