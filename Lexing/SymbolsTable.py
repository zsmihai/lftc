from bisect import bisect_left


class SymbolsTable:
    def __init__(self):
        self.__symbol_table = []
        self.__id_table = {}

    def insert_and_get_id(self, symbol):
        insert_position = bisect_left([symbol[0] for symbol in self.__symbol_table], symbol)

        if len(self.__symbol_table) == 0 or \
                        insert_position == len(self.__symbol_table) or \
                        self.__symbol_table[insert_position][0] is not symbol:
            id = len(self.__symbol_table)
            self.__symbol_table.insert(insert_position, (symbol, id))
            self.__id_table[id] = symbol
        else:
            id = self.__symbol_table[insert_position][1]

        return id

    def get_by_id(self, id):
        return self.__id_table[id]
