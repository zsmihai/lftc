import re
from Lexing.LexerException import LexerException
from Lexing.Token import gTwoCharOperators, Token, gOneCharOperatorsSeparators, TokenId, gKeyWords

class Lexer:

    __MAX_IDENTIFIER_LENGTH = 8

    def __init__(self, filename):
        self.__current_line = 0
        self.__current_column = 0
        self.__filename = filename
        self.__string_constant_regex = re.compile("\"[a-zA-Z0-9]*\"")
        self.__numeric_constant_regex = re.compile("(?P<number>(0|([1-9][0-9]*)))[^a-zA-Z]")
        self.__identifier_regex = re.compile("[a-zA-Z][a-zA-Z0-9]*")
        self.__whitespace_regex = re.compile("[ \t\r]*[\n]?")

    def get_tokens(self):
        with open(self.__filename, "r") as file:
            for line in file:
                self.__current_line += 1
                for token in self.__parse_line(line):
                    yield token

    def __match_two_char_operator(self, line, start):
        token = line[start:start+2]
        if len(token) != 2:
            return None

        token_id = gTwoCharOperators.get(token, None)
        if token_id is not None:
            self.__current_column += len(token)
            return Token(token_id=token_id, token_string=token)

        return None

    def __match_one_char_operator(self, line, start):
        token = line[start:start + 1]
        if len(token) != 1:
            return None

        token_id = gOneCharOperatorsSeparators.get(token, None)
        if token_id is not None:
            self.__current_column +=len(token)
            return Token(token_id=token_id, token_string=token)

        return None

    def __match_string_constant(self, line, start):
        regex_match = self.__string_constant_regex.match(line, pos = start)

        if regex_match:
            token_string = regex_match.group(0)
            self.__current_column += len(token_string)
            return Token(token_id=TokenId.TKN_CONSTANT, token_string=token_string)

        return None

    def __match_numeric_constant(self, line, start):
        regex_match = self.__numeric_constant_regex.match(line, pos=start)

        if regex_match:
            token_string = regex_match.group("number")
            self.__current_column += len(token_string)
            return Token(token_id=TokenId.TKN_CONSTANT, token_string=token_string)

        return None

    def __match_identifier(self, line, start):
        regex_match = self.__identifier_regex.match(line, pos = start)

        if regex_match:
            token_string = regex_match.group(0)
            self.__current_column += len(token_string)

            keyword_id = gKeyWords.get(token_string, None)

            if keyword_id is not None:
                return Token(token_id = gKeyWords[token_string], token_string = token_string)

            if len(token_string) > Lexer.__MAX_IDENTIFIER_LENGTH:
                raise LexerException("Identifier exceedes max identifier length: {0}".format(Lexer.__MAX_IDENTIFIER_LENGTH),
                                     self.__current_line, self.__current_column )

            return Token(token_id = TokenId.TKN_IDENTIFIER,token_string = token_string)

        return None

    def __consume_whitespace(self, line, start):
        regex_match = self.__whitespace_regex.match(line, start)
        if regex_match:
            self.__current_column += len(regex_match.group(0))


    def __parse_line(self, line):
        self.__current_column = 0
        self.__consume_whitespace(line, self.__current_column)
        while self.__current_column < len(line):

            token = self.__match_two_char_operator(line, self.__current_column)

            if token is None:
                token = self.__match_one_char_operator(line, self.__current_column)
            if token is None:
                token = self.__match_string_constant(line, self.__current_column)
            if token is None:
                token = self.__match_numeric_constant(line, self.__current_column)
            if token is None:
                token = self.__match_identifier(line, self.__current_column)

            if token is None:
                raise LexerException("Unidentified token", self.__current_line, self.__current_column)

            yield token
            self.__consume_whitespace(line, self.__current_column)
