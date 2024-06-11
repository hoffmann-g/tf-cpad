from reader import Reader
from utils import format_columns, replace_columns

base_source = './data/2020/'

def main():
    df = format_columns(Reader.to_dbf(input=base_source+'SPRS2001.dbc', output=base_source+'SPRS2001.dbf'))
    replace_columns(df)
    print(df)
    df.to_csv(base_source+'SPRS2001.csv', sep=',', index=False, encoding='utf-8', escapechar='\n')

if __name__ == '__main__':
    main()