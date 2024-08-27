from io import StringIO
import pandas as pd
from pretty_html_table import build_table


def csv_to_html_table(list_csv: list):
    if len(list_csv) == 2 and list_csv[1] == 400:
        return list_csv[0], list_csv[1]

    string_csv = ""

    for i in list_csv:
        string_csv += i + "\n"

    df = pd.read_csv(StringIO(string_csv), sep=";")
    df = df.fillna("")

    for i in df.columns:
        if i.find("Unnamed") != -1:
            df.rename(columns={i: ''}, inplace=True)

    html_table = build_table(df, 'blue_light')
    return html_table
