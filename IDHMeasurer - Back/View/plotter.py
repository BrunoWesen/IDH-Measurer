import pandas as pd
import plotly.express as px


def line_bar_plot(list1, list2, list3, obj_names):
    data_line_y = list1
    data_line_x = list2
    bar = list3
    fig = px.line(x=data_line_x, y=data_line_y, color=px.Constant(obj_names[0]),
                  color_discrete_map={
                      obj_names[0]: 'blue',
                  }, title=obj_names[2] + " por " + obj_names[1].lower() + " e " + obj_names[0].lower(),
                  labels=dict(x=obj_names[1], y=obj_names[2], color="Legenda"))
    fig.add_bar(x=data_line_x, y=bar, name=obj_names[2])
    fig.update_traces(marker_color='limegreen')
    fig.write_html("templates/plot_line_bar.html")
    return "plot_line_bar.html"


def line_plot(list1, list2, list3, obj_names):
    data_line_x = list1
    data_line_y = list2
    data_line_y_2 = list3
    df = pd.DataFrame({
        obj_names[0]: data_line_x,
        obj_names[1]: data_line_y,
        obj_names[2]: data_line_y_2,
    })
    fig = px.line(df, x=obj_names[0], y=[obj_names[1], obj_names[2]], title="{} {} X {} por {}".format(obj_names[3],
                                                                                                       obj_names[1],
                                                                                                       obj_names[2],
                                                                                                       obj_names[0]
                                                                                                       .lower()))
    fig.update_traces(hovertemplate='Ano: %{x}<br>' + obj_names[3] + ': %{y}%')
    fig.update_layout(yaxis_title=obj_names[3], legend_title="Legenda", hovermode="x")
    fig.write_html("templates/plot_line.html")
    return "plot_line.html"


def bar_plot(list1, list2, obj_names):
    data_line_x = list1
    data_line_y = list2
    df = pd.DataFrame({
        obj_names[0]: data_line_x,
        obj_names[1]: data_line_y,
    })
    fig = px.bar(df, x=obj_names[0], y=obj_names[1], title="{} por {}".format(obj_names[1], obj_names[0].lower()))
    fig.update_traces(hovertemplate=obj_names[0] + ': %{x}<br>' + obj_names[1][:-4] + ': %{y}%',
                      marker_color='limegreen')
    fig.write_html("templates/plot_bar.html")
    return "plot_bar.html"
