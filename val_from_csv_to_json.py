from val_converter_file_format import Converter

class CSV_JSON(Converter):

    def read_header(self):
        pass

    def record_value(self):
        pass

    def __init__(self, file_csv):
        self.nmcsv = file_csv
        self.data_csv = []          #храниние получаемой инфу(rows) из файла
        self.open()                 #прочитать файл
        self.data_cell, self.data_global = [], []
        self.out_data_json = []

    def close(self):
        pass

    #return rows of the csv file
    def open(self):
        with open(self.nmcsv, 'r') as fl:
            for line in fl:
                self.data_csv.append(line.strip('\n'))

    def common_action(self, line, pttrn):
        last_poss = line.find(pttrn)
        if last_poss == -1:
            self.data_cell.append(line[0:])
            line = None
            return None
        try:
            if line[last_poss+1] == ",":
                self.data_cell.append(line[0:last_poss+1])
            else: self.data_cell.append(line[0:last_poss])
        except IndexError as er:
            pass

        line= line[last_poss + 1:]
        return line

    def seek_data_cell(self, line):

        """
            если строка(ячейка) начинается на " то етсь предложени, то мы ищем конец этой строки
            то есть символы ",
        """
        """
            если строка начинается с ' то есть цисло , то мы ищем просто ',
        """
        """
            если это одно слово/символ
        """
        """
            если первый сивол это пробел
        """
        #print(type(line), line)
        if line == "" or line == None: return None

        elif line[0] == '"':
            #if str is some words ".... ....., ..."
            line = self.common_action(line, '",')

        elif line[0] == "'":
            line = self.common_action(line, "'")

        elif line[0].isalpha() == True or line[0].isdigit() == True:
            #if str without ',' in line
            line = self.common_action(line, ',')

        elif line[0] == ' ' or line[0] == ',':
            line = line[1:]

        else:
            line = self.common_action(line,',')


        self.seek_data_cell(line)


    def get_header_cell(self, index):
        return self.data_global[0][index]

    def record_to_file(self):

        for i in range(1, len(self.data_global) -1):

            data_cell = dict()
            for j in range(0,2):
                data_cell[self.get_header_cell(index=j)] = self.data_global[i][j]
            self.out_data_json.append(data_cell)

        with open(f"{self.nmcsv.split('.')[0]}.json", "w") as _json:
            _json.write(str(self.out_data_json))


    def start(self):
        rows = self.data_csv
        for row in rows:
            self.seek_data_cell(row)
            self.data_global.append(self.data_cell)
            #print(self.data_cell)
            self.data_cell = []

        self.record_to_file()














