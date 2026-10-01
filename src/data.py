import pandas as pd

# Load data
def data_loader(path):
    """ 
    Loads the dataset

    Args:
        You must provide the path of the dataset

    Returns:
        Dataframe of the dataset    
    """
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        print(f"An error occured:\n{e}")    