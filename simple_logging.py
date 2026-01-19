import logging
from datetime import datetime

def log_error(filename, error_message):
    """
    Log an error message to the specified file with a timestamp.

    Args:
        filename (str): The file to log errors to.
        error_message (str): The error message to log.
    """
    with open(filename, 'a') as f:
        f.write(f"{datetime.now()}: {error_message}\n")

def division(a, b):
    """
    Perform division and return the result.

    Args:
        a (float): Numerator.
        b (float): Denominator.

    Returns:
        float: The result of division.

    Raises:
        ZeroDivisionError: If the denominator is zero.
    """
    return a / b

def dictionary_lookup(dictionary, key):
    """
    Look up a key in a dictionary.

    Args:
        dictionary (dict): The dictionary to search.
        key: The key to find.

    Returns:
        The value associated with the key.

    Raises:
        KeyError: If the key is not in the dictionary.
    """
    return dictionary[key]

def parsefile(filename):
    """
    Read the contents of a file.

    Args:
        filename (str): The name of the file to read.

    Returns:
        list: A list of lines from the file.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    with open(filename, 'r') as f:
        return f.readlines()

def main():
    error_log_file = "errors.txt"
    
    try:
        result = division(10, 0)
    except ZeroDivisionError as e:
        log_error(error_log_file, f"ZeroDivisionError: {str(e)}")
    
    sample_dict = {"a": 1, "b": 2}
    try:
        value = dictionary_lookup(sample_dict, "c")  # 'c' does not exist
    except KeyError as e:
        log_error(error_log_file, f"KeyError: {str(e)}")
    
    try:
        lines = parsefile("nonexistent_file.txt")
    except FileNotFoundError as e:
        log_error(error_log_file, f"FileNotFoundError: {str(e)}")
    
    try:
        result = division(10, 2)  
        print("Division successful:", result)
    except ZeroDivisionError as e:
        log_error(error_log_file, f"ZeroDivisionError: {str(e)}")

if __name__ == '__main__':
    main()
