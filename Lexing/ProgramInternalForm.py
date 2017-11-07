from Lexing.SymbolsTable import SymbolsTable
from Lexing.Token import TokenId


class ProgramInternalForm:
    class InternalFormElement:
        def __init__(self, token_id, id):
            self.token_id = token_id
            self.id = id

    def __init__(self):
        self.__identifier_table = SymbolsTable()
        self.__constant_table = SymbolsTable()
        self.__tokens = []

    def add_token(self, token):
        if token.tokenId == TokenId.TKN_CONSTANT:
            self.add_constant(token.tokenString)
        elif token.tokenId == TokenId.TKN_IDENTIFIER:
            self.add_identifier(token.tokenString)
        else:
            self.add_token_by_id(token.tokenId)

    def add_identifier(self, identifier):
        id = self.__identifier_table.insert_and_get_id(identifier)
        self.__tokens.append(ProgramInternalForm.InternalFormElement(TokenId.TKN_IDENTIFIER, id))

    def add_constant(self, constant):
        id = self.__constant_table.insert_and_get_id(constant)
        self.__tokens.append(ProgramInternalForm.InternalFormElement(TokenId.TKN_CONSTANT, id))

    def add_token_by_id(self, token_id):
        self.__tokens.append(ProgramInternalForm.InternalFormElement(token_id, -1))
