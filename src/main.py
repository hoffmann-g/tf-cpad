from reader import from_dbf_to_dataframe 
from utils import format_columns, replace_columns
from pysus.ftp.databases.sih import SIH

base_source = './data/'
base_year = '2015'
month = "03"

def main():
    sih = SIH().load()
    # Get files from complete year
    # files = sih.get_files("RD", uf="SP", year=2000)
    files = sih.get_files("RD", uf="RS", year=2015, month=[1])
    parquets = sih.download(files, local_dir=base_source)
    df = parquets.to_dataframe()
    df.info()
    df_first_1000 = df.head(1000)
    df_first_1000 = format_columns(df_first_1000)
    replace_columns(df_first_1000)
    print(df_first_1000)

    # df_first_1000.to_csv(oputput_csv_file, sep=',', index=False, encoding='utf-8', escapechar='\n')

if __name__ == '__main__':
    main()
