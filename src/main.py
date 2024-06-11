from reader import Reader

def main():
    Reader.to_dbf(input='./data/2020/SPRS2001.dbc', output='./data/2020/SPRS2001.dbf')
    print('Hello World')

if __name__ == '__main__':
    main()