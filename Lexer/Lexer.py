import re

class Lexer:

    def __init__(self, filename):
        self.__current_line = 0
        self.__current_column = 1
        self.__filename = filename

    def get_tokens(self):
        with open(self.__filename, "r") as file:
            for line in file:
                self.__parse_line(line)

    def __parse_line(self, line):
        start = 0
        end = len(line)




