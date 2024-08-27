from Statistics_and_ML.nn_sequencial_model import sequencial_model_predict as SMP


def last_index_inputer_format(array: list, obj_name: str = "", city_name: str = "", cache=False):
    if obj_name != "":  # obj_name = Name of variable (eg: obj_name = rent)
        try:
            file = open("Data/Cache/" + city_name + ".city", "r")
            file = file.read().split(":")
            file.pop()

            for i in range(int(len(file) / 2)):
                if file[i * 2].find(obj_name) != -1:
                    data = file[i * 2 + 1][1:-1].split(", ")

                    try:
                        data = list(map(int, data))

                    except ValueError:
                        data = list(map(float, data))

                    return data

        except FileNotFoundError:
            pass

        missing_values_qtd = array.count("")
        data = list(SMP(array[:-missing_values_qtd], missing_values_qtd))

        if cache:
            file = open("Data/Cache/" + city_name + ".city", "a")
            file.write(obj_name + ":" + str(data) + ":")

        return data

    missing_values_qtd = array.count("")
    data = list(SMP(array[:-missing_values_qtd], missing_values_qtd))
    return data
