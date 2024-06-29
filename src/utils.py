from pandas import DataFrame, to_datetime

f_columns={"UF_ZI": "Cod_Zona_Municipio",
           "ESPEC": "Especialidade",
           "MUNIC_RES": "Municipio_Paciente",
           "QT_DIARIAS": "Diarias",
           "DT_INTER": "Data_Internacao",
           "DT_SAIDA": "Data_Saida",
           "DIAG_PRINC": "Diagnostico",
           "DIAG_SECUN": "Diagnostico_Secundario",
           "COBRANCA": "Motivo_Saida_Permanencia",
           "COD_IDADE": "Formato_Idade",
           "IDADE": "Idade",
           "DIAS_PERM": "Permanencia",
           "MORTE": "Morte",
           "NUM_FILHOS": "Filhos",
           "INSTRU": "Grau_Instrucao",
           "CID_NOTIF": "CID_Notificacao",
           "INFEHOSP": "Infeccao_Hospitalar",
           "CID_ASSO": "CID_Causa",
           "CID_MORTE": "CID_Morte",
           "DIAGSEC1": "Diagnostico_Secundario_1",
           "DIAGSEC2": "Diagnostico_Secundario_2",
           "DIAGSEC3": "Diagnostico_Secundario_3",
           "DIAGSEC4": "Diagnostico_Secundario_4",
           "DIAGSEC5": "Diagnostico_Secundario_5",
           "DIAGSEC6": "Diagnostico_Secundario_6",
           "DIAGSEC7": "Diagnostico_Secundario_7",
           "DIAGSEC8": "Diagnostico_Secundario_8",
           "DIAGSEC9": "Diagnostico_Secundario_9",
           "TPDISEC1": "Tipo_Diagnostico_1",
           "TPDISEC2": "Tipo_Diagnostico_2",
           "TPDISEC3": "Tipo_Diagnostico_3",
           "TPDISEC4": "Tipo_Diagnostico_4",
           "TPDISEC5": "Tipo_Diagnostico_5",
           "TPDISEC6": "Tipo_Diagnostico_6",
           "TPDISEC7": "Tipo_Diagnostico_7",
           "TPDISEC8": "Tipo_Diagnostico_8",
           "TPDISEC9": "Tipo_Diagnostico_9"}

to_be_removed_columns = ["ANO_CMPT",
             "MES_CMPT",
             "CGC_HOSP",
             "N_AIH",
             "IDENT",
             "CEP",
             "NASC",
             "SEXO",
             "UTI_MES_IN",
             "UTI_MES_AN",
             "UTI_MES_AL",
             "UTI_MES_TO",
             "MARCA_UTI",
             "UTI_INT_IN",
             "UTI_INT_AN",
             "UTI_INT_AL",
             "UTI_INT_TO",
             "DIAR_ACOM",
             "PROC_SOLIC",
             "PROC_REA",
             "VAL_SH",
             "VAL_SP",
             "VAL_SADT",
             "VAL_RN",
             "VAL_ACOMP",
             "VAL_ORTP",
             "VAL_SANGUE",
             "VAL_SADTSR",
             "VAL_TRANSP",
             "VAL_OBSANG",
             "VAL_PED1AC",
             "VAL_TOT",
             "VAL_UTI",
             "US_TOT",
             "DT_INTER",
             "NATUREZA",
             "NAT_JUR",
             "GESTAO",
             "RUBRICA",
             "IND_VDRL",
             "MUNIC_MOV",
             "NACIONAL",
             "NUM_PROC",
             "CAR_INT",
             "TOT_PT_SP",
             "CPF_AUT",
             "HOMONIMO",
             "CONTRACEP1",
             "CONTRACEP2",
             "GESTRISCO",
             "INSC_PN",
             "SEQ_AIH5",
             "CBOR",
             "CNAER",
             "VINCPREV",
             "GESTOR_COD",
             "GESTOR_TP",
             "GESTOR_CPF",
             "GESTOR_DT",
             "CNES",
             "CNPJ_MANT",
             "COMPLEX",
             "FINANC",
             "FAEC_TP",
             "REGCT",
             "RACA_COR",
             "ETNIA",
             "SEQUENCIA",
             "REMESSA",
             "AUD_JUST",
             "SIS_JUST",
             "VAL_SH_FED",
             "VAL_SP_FED",
             "VAL_SH_GES",
             "VAL_SP_GES",
             "VAL_UCI",
             "MARCA_UCI"]

# COD_IDADE (2 = "Dias"; 3 = "Meses" ; 4 = "Anos"; 0 = "")

# Limpeza dos dados:
# 0. remove_useless
# 1. Retirar colunas zeradas           -> remove_empty()
# 2. Renomear as colunas importantes   -> format_columns()
# 3. Retirar linhas onde o valor de alguma das colunas importantes forem zeradas -> dropna()
# 4. Retirar linhas com data saida ou data entrada diferentes do ano em questao (ex.: dados de 2015, porem tem linhas com datas em ano 2014)
# 5. Adicionar uma coluna com o ano, para permitir agrupamento mais facil no PowerBI
# 6. Transformar idade: ou concatenar numero + label (ex 3 anos, 2 dias) ou padronizar (transformar tudo para a mesma unidade de medida)
# 7. Analizar se QT_DIARIAS e DIAS_PERM sao iguais para todas as linhas
# 8. Transformar a idade: passar tudo para anos

def clear_data(df: DataFrame) -> DataFrame:
    # Remove colunas que nao nos interessam
    df = remove_useless(df)
    # Remove linhas com colunas sem informacao
    df = remove_empty(df)
    # Formata o nome das colunas
    df = format_columns(df)
    return df

def remove_useless(df: DataFrame) -> DataFrame:
    df = df.drop_duplicates()
    return df.drop(columns=to_be_removed_columns)

def remove_empty(df: DataFrame) -> DataFrame:
    df = df.dropna()
    return df

def format_columns(df: DataFrame) -> DataFrame:
    df = df.rename(columns=f_columns)
    # df = format_dates(df)
    df = transform_age(df)
    df = map_zi_to_name(df)
    return df

def format_dates(df: DataFrame) -> DataFrame:
    df['Data_Saida'] = df['Data_Saida'].apply(lambda x: to_datetime(x).strftime('%d/%m/%Y'))
    df['Data_Internacao'] = df['Data_Internacao'].apply(lambda x: to_datetime(x).strftime('%d/%m/%Y'))
    return df

def map_zi_to_name(df: DataFrame) -> DataFrame:
    #TODO: Converter códigos da coluna municipio para o nome de fato
    return df

def transform_age(df: DataFrame) -> DataFrame:

    return df