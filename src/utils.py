from pandas import DataFrame

f_columns={"SP_AA": "Ano", "SP_MM" : "Mês", "SP_UF" : "UF"}

def format_columns(df: DataFrame) -> DataFrame:
    return df.rename(columns=f_columns)

def replace_columns(df: DataFrame):
    df.loc[df['UF'] == '43', ['UF']] = 'RS'