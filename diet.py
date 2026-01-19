import pandas as pd

def parse_file(filename):
    """
    Load the CSV file into a DataFrame and display the column names.
    """
    df = pd.read_csv(filename)
    print("Column names:", df.columns)  
    return df

def search_food(df, food_name):
    """
    Search the DataFrame for rows where the 'name' column contains the given food_name.
    """
    return df[df['name'].str.contains(food_name, case=False, na=False)]

def test_search_food(df):
    """
    Test the search_food function with a sample food name.
    """
    result = search_food(df, "Apple")
    assert not result.empty, "Test failed: 'Apple' should be found in the dataset."

def main():
    """
    Main function to run the script.
    """
    filename = 'nutrition.csv'
    
    df = parse_file(filename)

    food_name = input("Enter a food name to search for: ")
    search_result = search_food(df, food_name)

    if not search_result.empty:
        print("Search results:")
        print(search_result)
    else:
        print(f"No results found for '{food_name}'.")

    test_search_food(df)
    print("Test passed: 'Apple' found in the dataset.")

if __name__ == '__main__':
    main()
