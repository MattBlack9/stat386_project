import pandas as pd 

def to_vector_of_strings(dataframe, column_name, exclude_words=None):
    """
    Converts into a vector of strings

    Parameters
    ----------

    dataframe : pandas dataframe
        The dataframe used for ...

    Returns
    -------
    y 
        An array of 
    """
    # Set default value for exclude_words
    exclude_words = exclude_words or []

    # Split words using commas and periods
    words_list = dataframe[column_name].str.lower().str.replace('.', ',').str.split(',').explode().str.strip().tolist()

    # Filter out values of empty strings
    words_list = [word for word in words_list if word and word not in exclude_words]
    # Create a new DataFrame with a row for each word
    vector_of_words = pd.DataFrame({
        '{}_word'.format(column_name): words_list
    })
    
    return vector_of_words
