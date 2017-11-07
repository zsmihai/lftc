class LexerException(BaseException):
    def __init__(self, message, line, column):
        self.message = message
        self.line = line
        self.column = column

    def __str__(self):
        return "Line {0}, column {1}: {2}".format(self.line, self.column, self.message)
