def binary_to_string(dataset, column_name, string_one, string_two):
    """
    This functions changes a binary variable into string format. This is meant to make a readable variable for data visualization.

    Parameters
        dataframe: The dataframe you want to perform the function on

        column_name: The column in the dataframe to perform the fuction on

        string_one: The string value that is associated with the binary variable value 1

        string_two: The string value that is associated with the binary variable value 2

    Returns
        Does not return any values, but makes a new column in the dataset using the original column name + "_str"

        
        
    """
    mapping = {1: string_one, 2: string_two}
    dataset[column_name + '_str'] = dataset[column_name].map(mapping)