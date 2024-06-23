from pandas import DataFrame

f_columns={"DT_SAIDA": "Data_saida", "DT_INTER" : "Data_internacao", "DIAS_PERM": "Dias_internacao_total", "UF_ZL" : "Municipio"}

# Colunas principais:
# UF_ZI
# ESPEC
# MUNIC_RES
# QT_DIARIAS
# DI_INTER
# DT_SAIDA
# DIAG_PRINC
# DIAG_SECUN
# COBRANCA
# COD_IDADE (2 = "Dias"; 3 = "Meses" ; 4 = "Anos"; 0 = "")
# IDADE
# DIAS_PERM
# MORTE
# NUM_FILHOS
# INSTRU
# CID_NOTIF
# INFEHOSP
# CID_ASSO
# CID_MORTE
# DIAGSEC1 a DIAGSEC9
# TPDISEC1 a TPDISEC9

# Limpeza dos dados:
# 1. Retirar colunas zeradas
# 2. Renomear as colunas importantes
# 3. Retirar linhas onde alguma das colunas importantes forem zeradas
# 4. Retirar linhas com data saida ou data internacao diferentes do ano em questao (ex.: dados de 2015, porem tem linhas com datas em ano 2014)
# 5. Adicionar uma coluna com o ano, para permitir agrupamento mais facil no PowerBI
# 6. Transformar idade: ou concatenar numero + label (ex 3 anos, 2 dias) ou padronizar (transformar tudo para a mesma unidade de medida)
# 7. Analizar se QT_DIARIAS e DIAS_PERM sao iguais para todas as linhas

def format_columns(df: DataFrame) -> DataFrame:
    return df.rename(columns=f_columns)

def replace_columns(df: DataFrame):
    df.loc[df['UF'] == '43', ['UF']] = 'RS'
