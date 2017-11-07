from Lexing.LexerException import LexerException
from Lexing.ProgramInternalForm import ProgramInternalForm
from Lexing.Lexer import Lexer

if __name__ == "__main__":
    pif = ProgramInternalForm()
    lxr = Lexer("..\\TestFiles\\a.in")

    try:
        for token in lxr.get_tokens():
            pif.add_token(token)
    except LexerException as e:
        print(e)
    print("done")

