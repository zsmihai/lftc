from Lexing.SymbolsTable import SymbolsTable
from Lexing.Token import TokenId


class InternalFormElement:
    def __init__(self, token_id, id):
        self.token_id = token_id
        self.id = id

class ProgramInternalForm:


    def __init__(self):
        self.identifier_table = SymbolsTable()
        self.constant_table = SymbolsTable()
        self.tokens = []

    def add_token(self, token):
        if token.tokenId == TokenId.TKN_CONSTANT:
            self.__add_constant(token.tokenString)
        elif token.tokenId == TokenId.TKN_IDENTIFIER:
            self.__add_identifier(token.tokenString)
        else:
            self.__add_token_by_id(token.tokenId)

    def __add_identifier(self, identifier):
        id = self.identifier_table.insert_and_get_id(identifier)
        self.tokens.append(InternalFormElement(TokenId.TKN_IDENTIFIER, id))

    def __add_constant(self, constant):
        id = self.constant_table.insert_and_get_id(constant)
        self.tokens.append(InternalFormElement(TokenId.TKN_CONSTANT, id))

    def __add_token_by_id(self, token_id):
        self.tokens.append(InternalFormElement(token_id, -1))


