from Lexer.SymbolsTable import SymbolsTable


class ProgramInternalForm:

    class InternalFormElement:
        def __init__(self, token_id, id):
            self.token_id = token_id
            self.id = id

    def __init__(self):
        self.__identifier_table = SymbolsTable()
        self.__constant_table = SymbolsTable()
        self.__tokens = []

    def add_token(self, token_id, id):
        self.__tokens.append(ProgramInternalForm.InternalFormElement(token_id, id))
