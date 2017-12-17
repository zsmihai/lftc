from Lexing.LexerException import LexerException
from Lexing.Lexer import Lexer
from Lexing.ProgramInternalForm import ProgramInternalForm


class Analizer:

    def __init__(self):
        pass

    @staticmethod
    def analize_file(filename):
        pif = ProgramInternalForm()
        lxr = Lexer(filename)
        try:
            for token in lxr.get_tokens():
                pif.add_token(token)

        except LexerException as ex:
            print(ex)
        Analizer.__write_symbol_table_to_file(filename, pif.identifier_table, ".ident")
        Analizer.__write_symbol_table_to_file(filename, pif.constant_table, ".const")
        Analizer.__write_program_internal_form_to_file(filename, pif.tokens, ".pif")

    @staticmethod
    def __write_symbol_table_to_file(input_file, symboltable, filemodifier):
        symbol_file_name = input_file + filemodifier
        with open(symbol_file_name, "w") as file:
            for identifier in symboltable.symbols():
                file.write("{0}  {1}\n".format(identifier[0], identifier[1]))

    @staticmethod
    def __write_program_internal_form_to_file(input_file, pif, filemodifier):
        pif_file_name = input_file + filemodifier
        with open(pif_file_name, "w") as file:
            for token in pif:
                file.write("{0} {1}\n".format(token.token_id.value, token.id))