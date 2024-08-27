import os
import shutil
import json
from zipfile import ZipFile

import requests
import pandas as pd


def loading_info_change(change=True):
    loading = {"download_file_function": change}
    file = open("Data/loading_info.json", "w")
    data = json.dumps(loading)
    file.write(data)
    file.close()


def download(year, context, filename):
    file = open("Data/loading_info.json", "r")
    data = json.load(file)
    file.close()

    if data["download_file_function"]:
        return "Essa operação já está em andamento no sistema..."

    loading_info_change()
    path_dir = "CollectedData/" + context + "/" + year
    path = path_dir + "/" + filename + ".csv"

    try:
        print("Verificando se o arquivo já está armazenado no banco de dados.")
        if os.path.exists(path):
            loading_info_change(False)
            return "Arquivo já está no banco de dados."

        os.mkdir(path_dir)

    except FileExistsError:
        pass

    print("Buscando por fontes!")
    if filename == "Matrícula":
        try:
            links = {
                "2022": "https://download.inep.gov.br/censo_escolar/resultados/2022/DOU_final_anexo_I.xlsx",
                "2021": "https://download.inep.gov.br/censo_escolar/resultados/2021/resultado_final_anexo_1_.xlsx",
                "2020": "https://download.inep.gov.br/educacao_basica/censo_escolar/resultado/2020/Anexo_I_2020_Final"
                        ".xlsx",
                "2019": "https://download.inep.gov.br/educacao_basica/censo_escolar/resultado/2019/anexo_I_final-2019"
                        ".xlsx",
                "2018": "https://download.inep.gov.br/educacao_basica/censo_escolar/resultado/2018/2018_final_anexo_I"
                        ".xlsx",
                "2017": "https://download.inep.gov.br/educacao_basica/censo_escolar/resultado/2017/dados_2017_Final_"
                        "Anexo_I.xlsx",
                "2016": "https://download.inep.gov.br/educacao_basica/censo_escolar/resultado/2016/retificacao_anexo_I"
                        ".xlsx",
                "2015": "https://download.inep.gov.br/educacao_basica/censo_escolar/resultado/2015/2015_resultados_"
                        "finais_censo_escolar_anexo_I.xlsx",
                "2014": "https://download.inep.gov.br/educacao_basica/censo_escolar/resultado/2014/Anexo_I_final_2014"
                        ".xlsx",
                "2013": "https://download.inep.gov.br/educacao_basica/censo_escolar/resultado/2013/Anexo_I_final_2013"
                        ".xlsx",
            }
            link = links[year]
            return downloader(link, path_dir, filename, True)

        except KeyError:
            loading_info_change(False)
            return "Infelizmente esse arquivo não está disponível na data fornecida."

    if filename == "Rendimento":
        try:
            links = {
                "2022": "https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2022/tx_rend_"
                        "municipios_2022.zip",
                "2021": "https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2021/tx_rend_"
                        "municipios_2021.zip",
                "2020": "https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2020/tx_rend_"
                        "municipios_2020.zip",
                "2019": "https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2019/tx_rend_"
                        "municipios_2019.zip",
                "2018": "https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2018/TX_REND_"
                        "MUNICIPIOS_2018.zip",
                "2017": "https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2017/TAXA_REND_"
                        "2017_MUNICIPIOS.zip",
                "2016": "https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2016/TAXA_REND_"
                        "2016_MUNICIPIOS.zip",
                "2015": "https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2015/taxa_"
                        "rendimento/tx_rendimento_municipios_2015.zip",
                "2014": "https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2014/taxa_"
                        "rendimento/tx_rendimento_municipios_2014.zip",
                "2013": "https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2013/taxa_"
                        "rendimento/tx_rendimento_municipios_2013.zip",
                "2012": "https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2012/taxas_"
                        "rendimento/tx_rendimento_municipios_2012.zip",
                "2011": "https://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/taxa_"
                        "rendimento/2011/tx_rendimento_municipios_2011_2.zip",
                "2010": "https://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/taxa_"
                        "rendimento/2010/tx_rendimento_municipios_2010.zip",
                "2009": "https://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/taxa_"
                        "rendimento/2009/tx_rendimento_municipios_2009.zip",
                "2008": "https://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/taxa_"
                        "rendimento/2008/tx_rendimento_municipios_2008.zip",
            }
            link = links[year]
            return downloader(link, path_dir, filename, True)

        except KeyError:
            loading_info_change(False)
            return "Infelizmente esse arquivo não está disponível na data fornecida."

    font = open("CollectedData/Fontes.txt", "r")
    font = font.read().split("\n")

    for i in font:
        if i.find(filename) != -1:
            link = i.split(":", 1)[1].replace("__ANO__", year)
            return downloader(link, path_dir, filename)


def downloader(link: str, path_dir: str, filename: str, trusted=False):
    print("Baixando arquivo...")
    response = requests.get(link, verify=False)
    path = path_dir + "/" + link.split("/")[-1]

    with open(path, 'wb') as file:
        if response.headers['Content-Type'].find(link.split(".")[-1]) != -1 or trusted:
            file.write(response.content)

        else:
            loading_info_change(False)
            return "Infelizmente esse arquivo não está disponível na data fornecida."

    print("Transformando arquivos baixados.")
    transform(path_dir, path, filename, link.split(".")[-1])

    print("Transformação concluída! Arquivo de \"" + filename + "\" Adicionado ao banco de dados!")
    loading_info_change(False)
    return 'Arquivo baixado e adicionado ao banco de dados com sucesso!'


def transform(path_dir, path, finalname, filetype):
    if filetype == "zip":
        z = ZipFile(path)
        filename = path.split("/")[-1].split(".")[0]
        filepath = ""

        for i in z.filelist:
            if i.filename.find(".xlsx") != -1 or i.filename.find(".xls") != -1:
                filepath = i.filename
                break

        if filepath == "":
            loading_info_change(False)
            return "Contate o seu Desenvolvedor (CÓD: transform_not_found_xl_115)"

        print("Extraindo arquivos...")
        z.extract(filepath, path=path_dir)
        z.close()
        file = pd.read_excel(path_dir + "/" + filepath)

        print("Convertendo arquivo para csv.")
        file.to_csv(path_dir + "/" + finalname + ".csv", index=None, header=True, sep=";")

        print("Removendo vestígios e otimizando espaço de armazenamento.")
        try:
            os.remove(path_dir + "/" + filepath)
            os.remove(path_dir + "/" + filename + ".zip")
            shutil.rmtree(path_dir + "/" + filename)
        except FileNotFoundError:
            pass

    elif filetype == "xlsx":
        filename = path.split("/")[-1].split(".")[0]

        print("Lendo arquivo.")
        file = pd.read_excel(path_dir + "/" + filename + ".xlsx")

        print("Convertendo arquivo para csv.")
        file.to_csv(path_dir + "/" + finalname + ".csv", index=None, header=True, sep=";")

        print("Removendo vestígios e otimizando espaço de armazenamento.")
        os.remove(path_dir + "/" + filename + ".xlsx")

    elif filetype == "csv":
        print("Renomeando arquivo...")
        os.rename(path, path_dir + "/" + finalname + ".csv")

