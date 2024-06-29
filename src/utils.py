from pandas import DataFrame, to_datetime

f_columns={"UF_ZI": "Cod_Zona_Municipio",
           "MUNIC_RES": "Municipio_Paciente",
           "SEXO": "Genero",
           "COD_IDADE": "Formato_Idade",
           "IDADE": "Idade",
           "ESPEC": "Especialidade",
           "DT_INTER": "Data_Internacao",
           "DT_SAIDA": "Data_Saida",
           "DIAG_PRINC": "Diagnostico",
           "QT_DIARIAS": "Diarias",
           "DIAS_PERM": "Permanencia",
           "COBRANCA": "Motivo_Saida_Permanencia",
           "MORTE": "Morte",
           "INFEHOSP": "Infeccao_Hospitalar",
           "CID_ASSO": "CID_Causa",
           "CID_MORTE": "CID_Morte"
           }

to_be_removed_columns = [
    "CID_NOTIF",
    "INSTRU",
    "NUM_FILHOS",
    "ANO_CMPT",
    "MES_CMPT",
    "CGC_HOSP",
    "N_AIH",
    "IDENT",
    "CEP",
    "NASC",
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
    "MARCA_UCI",
    "DIAGSEC1",
    "DIAGSEC2",
    "DIAGSEC3",
    "DIAGSEC4",
    "DIAGSEC5",
    "DIAGSEC6",
    "DIAGSEC7",
    "DIAGSEC8",
    "DIAGSEC9",
    "TPDISEC1",
    "TPDISEC2",
    "TPDISEC3",
    "TPDISEC4",
    "TPDISEC5",
    "TPDISEC6",
    "TPDISEC7",
    "TPDISEC8",
    "TPDISEC9",
    "DIAG_SECUN"]

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

def pre_process_data(df: DataFrame) -> DataFrame:
    # Remove colunas que nao nos interessam
    df = remove_useless(df)
    #Renomeia as colunas importantes
    df = df.rename(columns=f_columns)
    # Remove linhas com colunas sem informacao
    df = remove_empty(df)
    # Formata o nome das colunas
    df = format_columns(df)
    return df

def remove_useless(df: DataFrame) -> DataFrame:
    df = df.drop_duplicates()
    return df.drop(columns=to_be_removed_columns)

def remove_empty(df: DataFrame) -> DataFrame:
    key_columns=["Diagnostico", "Data_Internacao", "Data_Saida"]
    # Remove linhas onde o valor de alguma das colunas do subset seja vazio
    df = df.dropna(subset=key_columns)
    return df

def format_columns(df: DataFrame) -> DataFrame:
    df = format_dates(df)

    df = data_translations(df)

    # df = map_zi_to_name(df)
    return df

def format_dates(df: DataFrame) -> DataFrame:
    df['Data_Saida'] = df['Data_Saida'].apply(lambda x: to_datetime(x).strftime('%d/%m/%Y'))
    df['Data_Internacao'] = df['Data_Internacao'].apply(lambda x: to_datetime(x).strftime('%d/%m/%Y'))
    return df

def map_zi_to_name(df: DataFrame) -> DataFrame:
    #TODO: Converter códigos da coluna municipio para o nome de fato
    return df

def data_translations(df: DataFrame) -> DataFrame:
    df = translate_gender(df)
    df = translate_age_ident(df)
    return df

def translate_gender(df: DataFrame) -> DataFrame:
    replacement_dict = {"1": 'M', "2": 'F', "3": 'F', "0": "", "9": ""}
    df['Genero'] = df['Genero'].astype(str).replace(replacement_dict)
    return df

def translate_age_ident(df: DataFrame) -> DataFrame:
    replacement_dict = {"2": "Dias", "3": "Meses", "4": "Anos", "0": "", "5": ""}
    df['Formato_Idade'] = df['Formato_Idade'].replace(replacement_dict)
    return df
