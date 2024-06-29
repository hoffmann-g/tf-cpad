from utils import pre_process_data
from pysus.ftp.databases.sih import SIH

base_source = './data/'
base_year = '2015'
month = "03"

def main():
    sih = SIH().load()
    # Get files from all year
    # files = sih.get_files("RD", uf="SP", year=2000)
    files = sih.get_files("RD", uf="RS", year=2015, month=[1])
    parquets = sih.download(files, local_dir=base_source)
    df = parquets.to_dataframe()
    
    # df_head = df
    data = pre_process_data(df.head(10000))
    # df_head = data.head(10000)
    
    print(data.info())

    data.to_csv("data/output.csv", sep=',', index=False, encoding='utf-8', escapechar='\n')

if __name__ == '__main__':
    main()
