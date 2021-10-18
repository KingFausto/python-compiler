import re
from token import Token

class AnalizadorLexico:
    def __init__(self):
        self.keywords = {
            # operadores aritmeticos
            "+": "SUM",
            "-": "SUB",
            "/": "DIV",
            "=": "ASIGN",
            # separadores
            "(": "OPENSEP1",
            ")": "CLOSESEP1",
            "[": "OPENSEP2",
            "]": "CLOSESEP2",
            "{": "OPENSEP3",
            "}": "CLOSESEP3",
            ";": "SEP4",
            ",": "SEP5",
            # operadores relacionales
            ":V": "MENOR",
            "V:": "MAYOR",
            "=V": "MENIG",
            "V=": "MAYIG",
            "=_=": "IGUAL",
            "=n=": "NIGUAL",
            # operadores logicos
            "&_&": "AND",
            "¬_¬": "OR",
            "T_T": "NOT",
            # operadores condicionales
            "@_@": "WHILE",
            "#_#": "FOR",
            "o_O?": "IF",
            "O_O?": "ELIF",
            "O_o?": "ELSE",
            # auxiliares 
            "$_$": "RETURN",
            ">:O": "PRINT",
            ":O": "COMMENT",
            ">.>": "IN",
            ":S": "BREAK",
            "♥_♥": "FUN",
        }

    def crear_tokens(self, codigo):
        tokens = []
        for i in codigo:
            if i in self.keywords:
                tokens.append(Token(self.keywords[i], i))
            elif re.search(r'^\d+$', i):
                tokens.append(Token('INT', i))
            elif re.search(r'^\d+\.\d+$', i):
                tokens.append(Token('FLOAT', i))
            elif i[0] == '"':
                tokens.append(Token('STRING', i))
            else:
                tokens.append(Token('VAR', i))
        return tokens
