import time


class City:
    def __init__(self, city):
        self.__city__ = city

        arquivo = open("Data/codigo_das_cidades.txt", "r", encoding='utf-8')
        text = arquivo.read().split("\n")
        arquivo.close()

        self.__text__ = text
        self.__line_index__ = 0

        for index, i in enumerate(text):
            if i.find(city) != -1:
                self.__line_index__ = index

        if self.__line_index__ == 0:
            while True:
                print("CITY NOT FOUND: " + city)
                time.sleep(3)

    @property
    def city_code(self):
        code = self.__text__[self.__line_index__][self.__text__[self.__line_index__].find(":")+2:]

        if len(code) > 6:
            code = code[:-1]

        return code

    @property
    def city_ibge_code(self):
        code = self.__text__[self.__line_index__][self.__text__[self.__line_index__].find(":")+2:]
        return code

    @property
    def city_name(self):
        return self.__city__

    @property
    def city_state(self):
        state = "not found"
        idx = self.__line_index__

        while idx > 0:
            idx -= 1
            if len(self.__text__[idx][self.__text__[idx].find(":")+2:]) == 2:
                state = self.__text__[idx][self.__text__[idx].find("-")+1:self.__text__[idx].find(":")]
                return state

        return state

    @property
    def city_lower_name(self):
        return self.__city__.lower()

    @property
    def city_upper_name(self):
        return self.__city__.upper()
