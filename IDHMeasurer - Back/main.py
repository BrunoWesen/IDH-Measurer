from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin

from Controller import analyzes
from View.csv_processor import csv_to_html_table
from View import plotter

app = Flask("IDH Measurer - Back-End")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JSON_AS_ASCII'] = False

__city__ = "Manaus"  # Define a cidade do sistema
_city_ = analyzes.instance_city(__city__)  # Contém informações da cidade


@app.route("/")  # Não tem propósito
@cross_origin()
def home_page():
    return "<p>This is back-end of IDH Measurer Application!</p>" \
           "<p>Documentation: DevBoys Team</p>" \
           "<p>Contact us! <br/><br/> 2020003326@ifam.edu.br</p>"


@app.route("/Populacao", methods=['GET'])  # Retorna a População
@cross_origin()
def population():
    content = "2.255.903 (estimado - 2021)"
    return content


@app.route("/Idh", methods=['GET'])  # Retorna o IDH
@cross_origin()
def idh():
    content = "0,737 (2010)"
    return content


@app.route("/Ii", methods=['GET'])  # Retorna o II
@cross_origin()
def ii():
    content = "157,25 (2019)"
    return content


@app.route("/Educacao/1", methods=['GET'])  # Retorna uma tabela html de educação
@cross_origin()
def education_regis():
    year = 0

    try:
        year = int(request.args.get('year'))

    except (TypeError, ValueError):
        pass

    if request.args.get('year') == "true":
        content = analyzes.education_registration_table(_city_, True)
        return content

    if year != 0:
        content = analyzes.education_registration_table(_city_, False, str(year))
        return csv_to_html_table(content)

    content = analyzes.education_registration_table(_city_)
    return csv_to_html_table(content)


@app.route("/Educacao/1/Info", methods=['GET'])  # Retorna informações dessa requisição
@cross_origin()
def education_regis_info():
    if request.args.get('font') == "true":
        content = "Inep"
        return content

    if request.args.get('dict') == "true":
        content = "Os resultados referem-se à matrícula inicial na Creche, Pré-Escola, Ensino Fundamental e " \
                  "Ensino Médio (incluindo o médio integrado e normal magistério), no Ensino Regular e na " \
                  "Educação de Jovens e Adultos presencial Fundamental e Médio (incluindo a EJA integrada à " \
                  "educação profissional) das redes estaduais e municipais, urbanas e rurais em tempo parcial " \
                  "e integral e o total de matrículas nessas redes de ensino."
        return content


@app.route("/Educacao/2/Aprovacao", methods=['GET'])  # Retorna uma tabela html de aprovação
@cross_origin()
def education_rent_tx_apr():
    year = 0

    try:
        year = int(request.args.get('year'))

    except (TypeError, ValueError):
        pass

    if request.args.get('year') == "true":
        content = analyzes.education_tx_rend_aprov_table(_city_, True)
        return content

    if year != 0:
        content = analyzes.education_tx_rend_aprov_table(_city_, False, str(year))
        return csv_to_html_table(content)

    content = analyzes.education_tx_rend_aprov_table(_city_)
    return csv_to_html_table(content)


@app.route("/Educacao/2/Reprovacao", methods=['GET'])  # Retorna uma tabela html de reprovação
@cross_origin()
def education_rent_tx_repr():
    year = 0

    try:
        year = int(request.args.get('year'))

    except (TypeError, ValueError):
        pass

    if request.args.get('year') == "true":
        content = analyzes.education_tx_rend_reprov_table(_city_, True)
        return content

    if year != 0:
        content = analyzes.education_tx_rend_reprov_table(_city_, False, str(year))
        return csv_to_html_table(content)

    content = analyzes.education_tx_rend_reprov_table(_city_)
    return csv_to_html_table(content)


@app.route("/Educacao/2/Abandono", methods=['GET'])  # Retorna uma tabela html de abandono
@cross_origin()
def education_rent_tx_aban():
    year = 0

    try:
        year = int(request.args.get('year'))

    except (TypeError, ValueError):
        pass

    if request.args.get('year') == "true":
        content = analyzes.education_tx_rend_aban_table(_city_, True)
        return content

    if year != 0:
        content = analyzes.education_tx_rend_aban_table(_city_, False, str(year))
        return csv_to_html_table(content)

    content = analyzes.education_tx_rend_aban_table(_city_)
    return csv_to_html_table(content)


@app.route("/Educacao/2/Info", methods=['GET'])  # Retorna informações dessa requisição
@cross_origin()
def education_rent_tx_info():
    if request.args.get('font') == "true":
        content = "Inep"
        return content

    if request.args.get('dict') == "true":
        content = "Taxas de Rendimento Escolar (Aprovação, Reprovação e Abandono), segundo a Localização " \
                  "e a Dependência Administrativa, nos Níveis de Ensino Fundamental e Médio por série, " \
                  "segundo os municípios."
        return content


@app.route("/Renda/1", methods=['GET'])  # Retorna um dado sobre renda
@cross_origin()
def rent_pmpob():
    if request.args.get('year') == "true":
        content = analyzes.rent_poor_proportion_analysis(_city_, True)
        return content

    content = analyzes.rent_poor_proportion_analysis(_city_)
    return content


@app.route("/Renda/1/Info", methods=['GET'])  # Retorna informações dessa requisição
@cross_origin()
def rent_pmpob_info():
    if request.args.get('font') == "true":
        content = "Ipea"
        return content

    if request.args.get('dict') == "true":
        content = "Proporção de pobres é definido como proporção dos indivíduos com renda domiciliar " \
                  "per capita igual ou inferior a R$ 140,00 mensais, em reais de agosto de 2010. " \
                  "O universo de indivíduos é limitado àqueles que vivem em domicílios particulares permanentes."
        return content


@app.route("/Renda/2", methods=['GET'])  # Retorna um dado sobre renda
@cross_origin()
def rent_monthly_avg():
    if __city__ != "Manaus":
        return "Essa informação não está disponível para " + __city__

    if request.args.get('year') == "true":
        return "2020"

    content = "O salário médio mensal dos trabalhadores formais em 2020 da sua cidade é de: 3 " \
              "salários mínimos."
    return content


@app.route("/Renda/2/Info", methods=['GET'])  # Retorna informações dessa requisição
@cross_origin()
def rent_monthly_avg_info():
    if request.args.get('font') == "true":
        content = "Ibge"
        return content

    if request.args.get('dict') == "true":
        content = "Salário médio é uma estimativa do que um trabalhador cobra monetariamente, em média. " \
                  "Trabalhador formal é qualquer ocupação trabalhista, manual ou intelectual, com " \
                  "benefícios e Carteira de trabalho assinada. Salário mínimo é o valor mais baixo " \
                  "de salário que os empregadores podem legalmente pagar aos seus funcionários pelo tempo " \
                  "e esforço gastos na produção de bens e serviços no âmbito nacional, sendo salário " \
                  "mínimo de 2020: 1.039,00"
        return content


@app.route("/Renda/3", methods=['GET'])  # Retorna uma página html com gráfico
@cross_origin()
def rent_plot_rent_per_year():
    if __city__ == "Manaus":
        if request.args.get('year') == "true":
            content = analyzes.get_rent_pop_per_year_manaus(_city_, True)
            return content

        return render_template(plotter.line_bar_plot(*analyzes.get_rent_pop_per_year_manaus(_city_)))

    return "Essa informação não está disponível para " + __city__


@app.route("/Renda/3/Info", methods=['GET'])  # Retorna informações dessa requisição
@cross_origin()
def rent_plot_rent_per_year_info():
    if __city__ == "Manaus":
        if request.args.get('font') == "true":
            content = "PNAD"
            return content

        if request.args.get('dict') == "true":
            content = "Estimativas de população apresentadas por mil pessoas, taxas em percentual, rendimentos em " \
                      "reais. *Dados de rendimento de 2020 até 2022 foram estipulados por um modelo de " \
                      "aprendizagem de máquina."
            return content

    return "Essa informação não está disponível para " + __city__, 400


@app.route("/Renda/4", methods=['GET'])  # Retorna uma página html com gráfico
@cross_origin()
def rent_plot_eviction_mun_state_per_year():
    if request.args.get('year') == "true":
        content = analyzes.get_eviction_mun_state_per_year(_city_, True)
        return content

    return render_template(plotter.line_plot(*analyzes.get_eviction_mun_state_per_year(_city_)))


@app.route("/Renda/4/Info", methods=['GET'])  # Retorna informações dessa requisição
@cross_origin()
def rent_plot_eviction_mun_state_per_year_info():
    if request.args.get('font') == "true":
        content = "PNAD"
        return content

    if request.args.get('dict') == "true":
        content = "Estimativas de população apresentadas por mil pessoas, taxas em percentual, rendimentos em " \
                  "reais. *Dados de desocupação de algumas cidades de 2020 até 2022 foram estipulados por um " \
                  "modelo de aprendizagem de máquina."
        return content


@app.route("/Renda/5", methods=['GET'])  # Retorna uma página html com gráfico
@cross_origin()
def rent_plot_rent_pmpob_per_zone():
    if __city__ == "Manaus":
        if request.args.get('year') == "true":
            content = analyzes.get_rent_poor_proportion_per_zone_manaus(_city_, True)
            return content

        return render_template(plotter.bar_plot(*analyzes.get_rent_poor_proportion_per_zone_manaus(_city_)))

    return "Essa informação não está disponível para " + __city__, 400


@app.route("/Renda/5/Info", methods=['GET'])  # Retorna informações dessa requisição
@cross_origin()
def rent_plot_rent_pmpob_per_zone_info():
    if __city__ == "Manaus":
        if request.args.get('font') == "true":
            content = "Ipea"
            return content

        if request.args.get('dict') == "true":
            content = "Proporção de pobres é definido como proporção dos indivíduos com renda domiciliar " \
                      "per capita igual ou inferior a R$ 140,00 mensais, em reais de agosto de 2010. " \
                      "O universo de indivíduos é limitado àqueles que vivem em domicílios particulares permanentes."
            return content

    return "Essa informação não está disponível para " + __city__, 400


@app.route("/Saude/1", methods=['GET'])  # Retorna um dado sobre saúde
@cross_origin()
def health_cnes_quantity():
    if request.args.get('year') == "true":
        content = analyzes.health_establishment_quantity(_city_, True)
        return content

    content = analyzes.health_establishment_quantity(_city_)
    return content


@app.route("/Saude/1/Info", methods=['GET'])  # Retorna informações dessa requisição
@cross_origin()
def health_cnes_quantity_info():
    if request.args.get('font') == "true":
        content = "Cnes"
        return content


@app.route("/Saude/2", methods=['GET'])  # Retorna um dado sobre saúde
@cross_origin()
def health_sim_quantity():
    year = 0

    try:
        year = int(request.args.get('year'))

    except (TypeError, ValueError):
        pass

    if request.args.get('year') == "true":
        content = analyzes.health_mortality_quantity(_city_, True)
        return content

    if year != 0:
        content = analyzes.health_mortality_quantity(_city_, False, str(year))
        return content

    content = analyzes.health_mortality_quantity(_city_)
    return content


@app.route("/Saude/2/Info", methods=['GET'])  # Retorna informações dessa requisição
@cross_origin()
def health_sim_quantity_info():
    if request.args.get('font') == "true":
        content = "Ministério da Saúde"
        return content


@app.route("/Download-Files", methods=['GET'])  # Retorna o resultado final da operação
@cross_origin()
def update_database():
    year = request.args.get('year')
    context = request.args.get('context')
    filename = request.args.get('filename')
    return analyzes.insert_data(year, context, filename)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
