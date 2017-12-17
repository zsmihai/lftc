from enum import Enum


class TokenId(Enum):
    TKN_IDENTIFIER = 0
    TKN_CONSTANT = 1
    TKN_SEGMENT = 2
    TKN_DATA = 3
    TKN_CODE = 4
    TKN_END = 5
    TKN_IF = 6
    TKN_ELSE = 7
    TKN_WHILE = 8
    TKN_IN = 9
    TKN_OUT = 10
    TKN_AND = 11
    TKN_OR = 12
    TKN_NOT = 13
    TKN_EQUAL = 14
    TKN_LEFT_PAREN = 15
    TKN_RIGHT_PAREN = 16
    TKN_LEFT_SQR_BRACKET = 17
    TKN_RIGHT_SQR_BRACKET = 18
    TKN_LEFT_CRL_BRACKET = 19
    TKN_RIGHT_CRL_BRACKET = 20
    TKN_SEMICOLON = 21
    TKN_PLUS = 22
    TKN_MINUS = 23
    TKN_MULTIPLY = 24
    TKN_SLASH = 25
    TKN_PERCENT = 26
    TKN_DOUBLE_EQUAL = 27
    TKN_NOT_EQUAL = 28
    TKN_LESS = 29
    TKN_GREATER = 30
    TKN_LESS_OR_EQUAL = 31
    TKN_GREATER_OR_EQUAL = 32


gKeyWords = {
    "segment": TokenId.TKN_SEGMENT,
    "data": TokenId.TKN_DATA,
    "code": TokenId.TKN_CODE,
    "end": TokenId.TKN_END,
    "if": TokenId.TKN_IF,
    "else": TokenId.TKN_ELSE,
    "while": TokenId.TKN_WHILE,
    "in": TokenId.TKN_IN,
    "out": TokenId.TKN_OUT,
    "and": TokenId.TKN_AND,
    "or": TokenId.TKN_OR,
    "not": TokenId.TKN_NOT
}

gTwoCharOperators = {
    "==": TokenId.TKN_DOUBLE_EQUAL,
    "<=": TokenId.TKN_LESS_OR_EQUAL,
    ">=": TokenId.TKN_GREATER_OR_EQUAL,
    "!=": TokenId.TKN_NOT_EQUAL
}

gOneCharOperatorsSeparators = {
    "=": TokenId.TKN_EQUAL,
    "<": TokenId.TKN_LESS,
    ">": TokenId.TKN_GREATER,
    "+": TokenId.TKN_PLUS,
    "-": TokenId.TKN_MINUS,
    "*": TokenId.TKN_MULTIPLY,
    "/": TokenId.TKN_SLASH,
    "(": TokenId.TKN_LEFT_PAREN,
    ")": TokenId.TKN_RIGHT_PAREN,
    "[": TokenId.TKN_LEFT_SQR_BRACKET,
    "]": TokenId.TKN_RIGHT_SQR_BRACKET,
    "{": TokenId.TKN_LEFT_CRL_BRACKET,
    "}": TokenId.TKN_RIGHT_CRL_BRACKET
}


class Token:

    def __init__(self, token_string, token_id):
        self.tokenString = token_string
        self.tokenId = token_id
