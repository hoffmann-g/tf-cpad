from utils import clear_data
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

    df_first_1000 = clear_data(df_first_1000)
    
    print(df_first_1000)

    df_first_1000.to_csv("data/output.csv", sep=',', index=False, encoding='utf-8', escapechar='\n')

if __name__ == '__main__':
    main()
