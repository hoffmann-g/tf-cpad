import pyreaddbc # type: ignore
from simpledbf import Dbf5


class Reader:
    def to_dbf(input: str, output: str):
        pyreaddbc.dbc2dbf(infile=input, outfile=output)

        dbf = Dbf5(output)

        df = dbf.to_dataframe()
        print(df)
