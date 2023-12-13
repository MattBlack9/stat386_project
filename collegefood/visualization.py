def binary_to_string(dataset, column_name, string_one, string_two):
    """
    This functions changes a binary variable into string format. This is meant to make a readable variable for data visualization.

    Parameters:
        dataframe: The dataframe you want to perform the function on
        column_name(string): In string format, the column in the dataframe to perform the fuction on
        string_one(string): The string value that is associated with the binary variable value 1
        string_two(string): The string value that is associated with the binary variable value 2

    Returns:
        Does not return any values, but makes a new column in the dataset using the original column name + "_str"
    """
    mapping = {1: string_one, 2: string_two}
    dataset[column_name + '_str'] = dataset[column_name].map(mapping)

def to_vector_of_strings(dataframe, column_name):
    """
    Converts all the strings in a dataset's column into a vector of strings. Useful if there are multiple strings in a single row.

    Parameters:
        dataframe: The dataframe you want to perform the function on
        column_name(string): The column in the dataframe to perform the fuction on
    
    Returns:
        Array: An array of all the strings that are every row of the column
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
        column_name(string): The column in the dataframe to perform the fuction on
        words_to_replace(dictionary): A dictionary with the words you want to replace. Format is 'word_to_be_replace' : 'replacement_word'

    Returns:
        Dataframe: This function returns a dataframe with the replaced values.
    """
    # Replace words using the specified mapping
    for original_word, replacement_word in words_to_replace.items():
        dataframe[column_name] = dataframe[column_name].replace(original_word, replacement_word)

    # Group and sum the occurrences of each word
    grouped_data = dataframe.groupby(column_name, as_index=False).sum()

    return grouped_data