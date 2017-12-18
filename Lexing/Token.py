from enum import Enum


class TokenId(Enum):
    TKN_IDENTIFIER = 0
    TKN_CONSTANT = 1
    TKN_DATA = 2
    TKN_CODE = 3
    TKN_END = 4
    TKN_IF = 5
    TKN_ELSE = 6
    TKN_WHILE = 7
    TKN_IN = 8
    TKN_OUT = 9
    TKN_AND = 10
    TKN_OR = 11
    TKN_NOT = 12
    TKN_EQUAL = 13
    TKN_LEFT_PAREN = 14
    TKN_RIGHT_PAREN = 15
    TKN_LEFT_SQR_BRACKET = 16
    TKN_RIGHT_SQR_BRACKET = 17
    TKN_LEFT_CRL_BRACKET = 18
    TKN_RIGHT_CRL_BRACKET = 19
    TKN_SEMICOLON = 20
    TKN_PLUS = 21
    TKN_MINUS = 22
    TKN_MULTIPLY = 23
    TKN_SLASH = 24
    TKN_PERCENT = 25
    TKN_DOUBLE_EQUAL = 26
    TKN_NOT_EQUAL = 27
    TKN_LESS = 28
    TKN_GREATER = 29
    TKN_LESS_OR_EQUAL = 30
    TKN_GREATER_OR_EQUAL = 31
    TKN_INT = 32
    TKN_CHAR = 33
    TKN_ARRAY = 34
    TKN_COMMA = 35


gKeyWords = {
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
    "not": TokenId.TKN_NOT,
    "array": TokenId.TKN_ARRAY,
    "int": TokenId.TKN_INT,
    "char": TokenId.TKN_CHAR
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
    "%": TokenId.TKN_PERCENT,
    "/": TokenId.TKN_SLASH,
    "(": TokenId.TKN_LEFT_PAREN,
    ")": TokenId.TKN_RIGHT_PAREN,
    "[": TokenId.TKN_LEFT_SQR_BRACKET,
    "]": TokenId.TKN_RIGHT_SQR_BRACKET,
    "{": TokenId.TKN_LEFT_CRL_BRACKET,
    "}": TokenId.TKN_RIGHT_CRL_BRACKET,
    ",": TokenId.TKN_COMMA,
    ";": TokenId.TKN_SEMICOLON
}


class Token:

    def __init__(self, token_string, token_id):
        self.tokenString = token_string
        self.tokenId = token_id
