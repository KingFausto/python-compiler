import re
from token_ import Token


class AnalizadorLexico:
    def __init__(self):
        self.keywords = {
            # operadores aritmeticos
            "+": "SUM",
            "-": "SUB",
            "*": "MULT",
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
            "#_#": "SWITCH",
            ">.>": "CASE",
            "o_O?": "IF",
            "O_o?": "ELSE",
            # auxiliares
            "$_$": "RETURN",
            ">:O": "PRINT",
            ":O": "COMMENT",
            ":S": "BREAK"
        }

    def crear_tokens(self, codigo):
        tokens = []
        for i in codigo:
            if i == ":O":
                break
            elif i in self.keywords:
                tokens.append(Token(self.keywords[i], i))
            elif re.search(r"^\d+$", i):
                tokens.append(Token("INT", i))
            elif re.search(r"^\d+\.\d+$", i):
                tokens.append(Token("FLOAT", i))
            elif i[0] == '"':
                tokens.append(Token("STRING", i))
            elif i in ["True", "False"]:
                tokens.append(Token("BOOL", i))
            else:
                tokens.append(Token("VAR", i))
        return tokens
