import pyreaddbc # type: ignore
from simpledbf import Dbf5
from pandas import DataFrame
import os


def from_dbf_to_dataframe(input: str, output: str) -> DataFrame:
    if not os.path.exists(output):
        print('Generating DBF')
        pyreaddbc.dbc2dbf(infile=input, outfile=output)

    dbf = Dbf5(output)

    df = dbf.to_dataframe()
    return df
