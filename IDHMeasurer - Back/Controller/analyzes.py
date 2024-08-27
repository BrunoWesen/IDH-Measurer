from unidecode import unidecode

from Model.city import City
from Ultilities import inputers, download_files


def instance_city(_city_):
    return City(_city_)


def insert_data(year, context, filename):
    return download_files.download(year, context, filename)


def education_registration_table(_city_, get_year: bool = False, year="2022"):
    if get_year:
        return year

    try:
        arquivo = open("CollectedData/Educação/" + year + "/Matrícula.csv", "r")

    except FileNotFoundError:
        return ["Ano Indisponível", 400]

    text = arquivo.read().split("\n")
    arquivo.close()
    city_index = 0

    for index, i in enumerate(text):
        if i.find(unidecode(_city_.city_upper_name)) != -1:
            city_index = index

    if city_index == 0:
        return ["CITY NOT FOUND", 400]

    content = text[city_index:city_index + 6]

    for index, i in enumerate(content):
        content[index] = ";".join(i.split(";")[1:12])

    content.insert(0, "Unidades da Federacao Municipios/Dependencia Administrativa;creche-parcial;"
                      "creche-Integral;pre-parcial;pre-integral;e.f.iniciais-parcial;e.f.iniciais-integral;"
                      "e.f.finais-parcial;e.f.finais-integral;medio-parcial;medio-integral")
    return content


def education_tx_rend_aprov_table(_city_, get_year: bool = False, year="2021"):
    if get_year:
        return year

    try:
        arquivo = open("CollectedData/Educação/" + year + "/Rendimento.csv", "r", encoding="utf-8")

    except FileNotFoundError:
        return "Ano Indisponível", 400

    text = arquivo.read().split("\n")
    arquivo.close()
    city_index = 0

    for index, i in enumerate(text):
        if i.find(_city_.city_ibge_code) != -1:
            city_index = index
            break

    if city_index == 0:
        return ["CITY NOT FOUND: " + _city_.city_name, 400]

    city_index_end = 0

    for index, i in enumerate(text[city_index:]):
        if i.find(_city_.city_ibge_code) != -1:
            city_index_end = index

        else:
            break

    content = text[city_index:city_index + city_index_end + 1]
    content.insert(0, text[6])
    content.insert(1, text[7])

    for index, i in enumerate(content):
        aux = 4

        while aux > 0:
            i = i[i.find(";") + 1:]
            aux -= 1

        content[index] = i

    for index, i in enumerate(content):
        aux = 19
        new_content = ""

        while aux > 0:
            new_content += i[:i.find(";") + 1]
            i = i[i.find(";") + 1:]
            aux -= 1

        content[index] = new_content

    content[0] = "Nome do Município;Localização;Dependência Administrativa;" + ";".join(content[0].split(";")[3:])

    for index, i in enumerate(content):
        content[index] = i[:-1]

    return content


def education_tx_rend_reprov_table(_city_, get_year: bool = False, year="2021"):
    if get_year:
        return year

    try:
        arquivo = open("CollectedData/Educação/" + year + "/Rendimento.csv", "r", encoding="utf-8")

    except FileNotFoundError:
        return "Ano Indisponível", 400

    text = arquivo.read().split("\n")
    arquivo.close()
    city_index = 0

    for index, i in enumerate(text):
        if i.find(_city_.city_ibge_code) != -1:
            city_index = index

            break
    if city_index == 0:
        return ["CITY NOT FOUND: " + _city_.city_name, 400]

    city_index_end = 0

    for index, i in enumerate(text[city_index:]):
        if i.find(_city_.city_ibge_code) != -1:
            city_index_end = index

        else:
            break

    content = text[city_index:city_index + city_index_end + 1]
    content.insert(0, text[6])
    content.insert(1, text[7])
    first_part_content = []

    for index, i in enumerate(content):
        aux = 4

        while aux > 0:
            i = i[i.find(";") + 1:]
            aux -= 1

        content[index] = i
        aux = 3

        while aux > 0:
            first_part_content.append(i[:i.find(";") + 1])
            i = i[i.find(";") + 1:]
            aux -= 1

        aux = 18

        while aux > 0:
            i = i[i.find(";") + 1:]
            aux -= 1

        content[index] = i

    for index, i in enumerate(content):
        aux = 16
        new_content = ""

        while aux > 0:
            new_content += i[:i.find(";") + 1]
            i = i[i.find(";") + 1:]
            aux -= 1

        content[index] = first_part_content[0] + first_part_content[1] + first_part_content[2] + new_content
        first_part_content.pop(0)
        first_part_content.pop(0)
        first_part_content.pop(0)

    content[0] = "Nome do Município;Localização;Dependência Administrativa;" + ";".join(content[0].split(";")[3:])

    for index, i in enumerate(content):
        content[index] = i[:-1]

    return content


def education_tx_rend_aban_table(_city_, get_year: bool = False, year="2021"):
    if get_year:
        return year

    try:
        arquivo = open("CollectedData/Educação/" + year + "/Rendimento.csv", "r", encoding="utf-8")

    except FileNotFoundError:
        return "Ano Indisponível", 400

    text = arquivo.read().split("\n")
    arquivo.close()
    city_index = 0

    for index, i in enumerate(text):
        if i.find(_city_.city_ibge_code) != -1:
            city_index = index
            break

    if city_index == 0:
        return ["CITY NOT FOUND: " + _city_.city_name, 400]

    city_index_end = 0

    for index, i in enumerate(text[city_index:]):
        if i.find(_city_.city_ibge_code) != -1:
            city_index_end = index

        else:
            break

    content = text[city_index:city_index + city_index_end + 1]
    content.insert(0, text[6])
    content.insert(1, text[7])
    first_part_content = []

    for index, i in enumerate(content):
        aux = 4

        while aux > 0:
            i = i[i.find(";") + 1:]
            aux -= 1

        content[index] = i
        aux = 3

        while aux > 0:
            first_part_content.append(i[:i.find(";") + 1])
            i = i[i.find(";") + 1:]
            aux -= 1

        aux = 36

        while aux > 0:
            i = i[i.find(";") + 1:]
            aux -= 1

        content[index] = i

    for index, i in enumerate(content):
        aux = 16
        new_content = ""

        while aux > 0:
            new_content += i[:i.find(";") + 1]
            i = i[i.find(";") + 1:]
            aux -= 1

        content[index] = first_part_content[0] + first_part_content[1] + first_part_content[2] + new_content
        first_part_content.pop(0)
        first_part_content.pop(0)
        first_part_content.pop(0)

    content[0] = "Nome do Município;Localização;Dependência Administrativa;" + ";".join(content[0].split(";")[3:])

    for index, i in enumerate(content):
        content[index] = i[:-1]

    return content


def rent_poor_proportion_analysis(_city_, get_year: bool = False):
    if get_year:
        return "2010"

    arquivo = open("CollectedData/Renda/2000_2010/A - Base 20 RMs 2000_2010.csv", "r", encoding='utf-8')
    text = arquivo.read().split("\n")
    arquivo.close()
    idx = 0

    for index, i in enumerate(text):
        if i.find(_city_.city_name) != -1:
            idx = index

    content = "Proporção de pobres na sua cidade é de: " + text[idx].split(",")[57] + "% em 2010"
    return content


def get_rent_pop_per_year_manaus(_city_, get_year: bool = False):
    if get_year:
        return "2012 - 2022"

    arquivo = open("CollectedData/Renda/2012-2022/PNAD_continua_retrospectiva_regional_2012_2022.csv",
                   "r", encoding='utf-8')
    text = arquivo.read().split("\n")
    arquivo.close()
    population = []
    year = [2022]
    rent = []

    for index, i in enumerate(text):  # Get population
        if i.find("Amazonas") != -1:
            aux = int(float(year[0]) - 2012 + 1)

            while aux > 0:
                aux_i = i[i.find("\"") + 1:]
                i = aux_i[:aux_i.find("\"")]
                population.append(i)
                i = text[index][text[index].find(i) + len(i) + 1:]
                aux -= 1

            for idx, j in enumerate(population):
                j = j.replace(",", "")
                population[idx] = int(float(j) / 2)

            break

    for index, i in enumerate(population):  # Get years
        if len(population) == len(year):
            break

        year.append(int(year[index] - 1))

    year.reverse()
    aux = 3

    for index, i in enumerate(text):  # Get average rent
        if i.find("Manaus") != -1:
            aux -= 1

            if aux == 0:
                aux = len(year)

                if i[i.find("\"") + 1:].find("a") != -1:
                    aux_i = i[i.find("\"") + 1:]
                    i = aux_i[:aux_i.find("\"")]
                    text[index] = text[index][text[index].find(i) + len(i) + 1:]
                    i = text[index]

                while aux > 0:
                    if i.find("\"") == -1 and aux > 0:
                        for j in range(aux):
                            rent.append('')

                        break

                    aux_i = i[i.find("\"") + 1:]
                    i = aux_i[:aux_i.find("\"")]
                    rent.append(int(i.replace(",", "")))
                    i = text[index][text[index].find(i) + len(i) + 1:]
                    aux -= 1

                break

    rent = inputers.last_index_inputer_format(rent, 'rent', _city_.city_name, True)

    return population, year, rent, ["População Total", "Ano", "Renda"]


def get_eviction_mun_state_per_year(_city_, get_year: bool = False):
    if get_year:
        return "2012 - 2022"

    arquivo = open("CollectedData/Renda/2012-2022/PNAD_continua_retrospectiva_regional_2012_2022.csv",
                   "r", encoding='utf-8')
    text = arquivo.read().split("\n")
    arquivo.close()
    mun_eviction = []
    state_eviction = []
    year = [2022]

    for index, i in enumerate(text):  # Get state eviction
        if i.find(_city_.city_state) != -1 != i.find("Taxa de desocupação"):
            state_eviction = i.split(",")[5: 5 + int(float(year[0]) - 2012 + 1)]
            state_eviction = list(map(float, state_eviction))
            break

    for index, i in enumerate(state_eviction):  # Get years
        if len(state_eviction) == len(year):
            break

        year.append(int(year[index] - 1))

    year.reverse()

    for index, i in enumerate(text):  # Get mun eviction
        if i.find(_city_.city_name) != -1 != i.find("Taxa de desocupação"):
            mun_eviction = i.split(",")[5: 5 + len(year)]
            break

    for index, i in enumerate(mun_eviction):
        try:
            mun_eviction[index] = float(i)

        except ValueError:
            mun_eviction[index] = ""

    mun_eviction = inputers.last_index_inputer_format(mun_eviction, 'mun_eviction', _city_.city_name, True)
    return year, mun_eviction, state_eviction, ["Ano", _city_.city_name, _city_.city_state, "Taxa de desocupação"]


def get_rent_poor_proportion_per_zone_manaus(_city_, get_year: bool = False):
    if get_year:
        return "2010"

    arquivo = open("CollectedData/Renda/2000_2010/RM 61300 Manaus - Base REGIONAL 2000_2010.csv", "r", encoding='utf-8')
    text = arquivo.read().split("\n")
    arquivo.close()
    idx = text[0].split(";").index("PMPOB")
    zones = []
    pmpob = []

    for i in text[10:-1]:
        line = i.split(";")
        line.pop()

        try:
            line[1][34]
            zones.append(line[1][:35] + "...)")

        except IndexError:
            zones.append(line[1][:])

        pmpob.append(float(line[idx]))

    return zones, pmpob, ["Zona", "Proporção de pobres (%)"]


def health_establishment_quantity(_city_, get_year: bool = False):
    if get_year:
        return "2023"

    arquivo = open("CollectedData/Saúde/2023/cnes_estabelecimentos.csv", "r")
    text = arquivo.read().split("\n")
    arquivo.close()
    text.pop()
    elements = []

    for i in text:
        elements.append(i.split(";")[3])

    content = _city_.city_name + " possui: " + str(elements.count(_city_.city_code)) + " estabelecimentos de saúde."

    return content


def health_mortality_quantity(_city_, get_year: bool = False, year="2020"):
    if get_year:
        return year

    try:
        arquivo = open("CollectedData/Saúde/" + year + "/Mortalidade.csv", "r")

    except FileNotFoundError:
        return "Ano Indisponível", 400

    text = arquivo.read().split("\n")
    arquivo.close()
    text.pop()
    index = text[0].split(";").index("\"CODMUNOCOR\"")
    elements = []

    for i in text:
        elements.append(i.split(";")[index])

    content = _city_.city_name + " possui: " + str(elements.count("\"" + str(_city_.city_code) + "\"")) + \
              " mortes em " + year + "."
    return content
