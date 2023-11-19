import pandas as pd


def get_country_data(dataset_path: str = "facts_countries.csv") -> pd.DataFrame:
    """Funkcija koja učitava CSV datoteku na dataset_path putanji. Nakon toga čisti podatke, uklanja NaN ćelije, 
    transponira podatke u DataFrameu i vraća takav DataFrame.

    Args:
        dataset_path (str, optional): Putanja do CSV datoteke. Zadano na -  "facts_countries.csv".

    Returns:
        pd.DataFrame: DataFrame s pročišćenim podacima.
    """
    df = pd.read_csv(dataset_path, sep=";", skiprows = [1])

    for column in df.columns:
        df[column].fillna(0, inplace=True)

    df_transposed = df.transpose()

    df_transposed.columns = df_transposed.iloc[0]
    df_transposed.columns = map(str.lower, df_transposed.columns)

    df_transposed = df_transposed[1:]

    return df_transposed

df = get_country_data()
# print(df)